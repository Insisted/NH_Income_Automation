"""
Another Version of nh_claim.py

Will be faster because not using GUI to do the task
Using POST/GET Request to do the task
"""

import json
import re
import sys
import time
from datetime import datetime, timedelta
from http import cookiejar
from pathlib import Path
from urllib import parse, request

import requests
from bs4 import BeautifulSoup


PATH = Path(__file__).parent
PERIOD = datetime.utcnow() + timedelta(hours=7)
PERIOD_D = PERIOD.replace(month=PERIOD.month%12+1, day=1) - timedelta(days=1)
LOGIN_URL = 'https://kageherostudio.com/payment/server_.php'
CLAIM_URL = 'https://kageherostudio.com/event/index_.php?act=daily'
EVENT_URL = 'https://kageherostudio.com/event/?event=daily'
USER_NAME = 'txtuserid'
PASS_NAME = 'txtpassword'
ITEM_POST = 'itemId'
PROD_POST = 'periodId'
SRVR_POST = 'selserver'
REWARD_CLS = '.reward-star'
REWARD_ATTR = 'data-id'


def main(data, num):
    start = data[num:]
    max_data = max(
        start,
        key=lambda x: (
            y := re.match(r'^.*(?=@)', x.get('username')).span()
        )[1] - y[0]
    )
    max_len = len(
        re.sub(r'@.*', '', max_data.get('username'))
    )

    for n, user in enumerate(start):
        _username = user.get('username')
        _password = user.get('password')
        _server = user.get('server')
        is_claimed = False

        print(f'{str(n+num+1)+".":<3} {re.sub(r"@.*", "", _username):<{max_len}}', end='')

        cookie_jar = login_cookie(_username, _password)

        session = requests.Session()
        session.cookies = cookie_jar

        html = session.get(EVENT_URL)
        sess_html = BeautifulSoup(
            html.text,
            'html.parser'
        )

        try: claim(session, sess_html, _server)
        except IndexError: is_claimed = True

        print_claimed(sess_html, is_claimed)
        time.sleep(1)

    else:
        print('SUCCEED!!!')


def claim(session, sess_html, server):
    item_id = sess_html.select(REWARD_CLS)[0][REWARD_ATTR]

    session.post(CLAIM_URL, data={
        ITEM_POST: item_id,
        PROD_POST: PERIOD.month,
        SRVR_POST: server,
    })


def print_claimed(sess_html, is_claimed):
    claimed = int(
        re.search(
            r'\d+',
            sess_html.select('h5')[0].text
        ).group()
    )

    print(
        f' {"ALREADY "*is_claimed}CLAIMED: {claimed+(not is_claimed)}/{PERIOD_D.day} DAY{"S"*(claimed > 1)}'
        if claimed
        else ' ERROR: Wrong Login Credential'
    )


def login_cookie(username, password):
    data = {
        USER_NAME: username,
        PASS_NAME: password,
    }
    login_data = parse.urlencode(data).encode('utf-8')

    cookie_jar = cookiejar.CookieJar()
    opener = request.build_opener(request.HTTPCookieProcessor(cookie_jar))

    # FIXME: This line took too long to finish the request
    #        Might have to change that in the future
    opener.open(LOGIN_URL, data=login_data)

    return cookie_jar


if __name__ == '__main__':
    with open(PATH / 'data.json', 'r') as json_file:
        data = json.load(json_file)

    if len(arg := sys.argv) > 1 and re.match(r'^\d+$', arg[1]):
        num = arg[1]
    else:
        print('\n'.join(f'{str(i+1)+".":<3} {j.get("username")}' for i, j in enumerate(data)))

        num = input(f'Starting Point(1 - {len(data)}): ')

        print()

    main(data, min(len(data), max(1, int(num)))-1)
