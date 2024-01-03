"""
Another Version of nh_claim.py

Will be faster because not using GUI to do the task
Using POST/GET Request to do the task
Now taking advantage of multithreading
"""

import concurrent.futures
import itertools
import json
import os
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

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
REWARD_PERIOD = 'data-period'


def main(data):
    max_data = max(
        map(
            lambda x: re.search(
                r'^.*(?=@)', x.get('username')
            ).group(),
            data
        ),
        key=len
    )
    max_len = len(max_data)

    # n_cores = os.cpu_count()
    n_threads = len(data)+1 # Will use all available threads relative to the data's length
    stop = [0]
    fails = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
        executor.submit(print_wait, stop)

        results = [executor.submit(user_claim, user) for user in data]

        for result, user in zip(concurrent.futures.as_completed(results), data):
            username = user.get('username')

            try:
                is_failed, message = result.result()
                fails += is_failed

                print(f'{re.sub(r"@.*", "", username):<{max_len}} {message}')
            except Exception as e:
                print(f'ERROR: {username} - {e}')

        stop.clear()

    print(f'{fails} failed attempt{"s"*(fails > 1)}' if fails else 'SUCCEED!!!')


def print_wait(stop):
    for dot in itertools.cycle(['.', '..', '...']):
        if not stop:
            break

        print(f'waiting{dot:<3}', end='\r')
        time.sleep(0.5)


def user_claim(user):
    _username = user.get('username')
    _password = user.get('password')
    _server = user.get('server')
    is_claimed = False

    session = requests.Session()

    login(session, _username, _password)

    html = session.get(EVENT_URL)
    sess_html = BeautifulSoup(
        html.text,
        'html.parser'
    )

    try: claim(session, sess_html, _server)
    except IndexError: is_claimed = True

    return check_claim(sess_html, is_claimed)


def claim(session, sess_html, server):
    item_id = sess_html.select(REWARD_CLS)[0][REWARD_ATTR]
    item_period = sess_html.select(REWARD_CLS)[0][REWARD_PERIOD]

    session.post(CLAIM_URL, data={
        ITEM_POST: item_id,
        PROD_POST: item_period,
        SRVR_POST: server,
    })


def check_claim(sess_html, is_claimed):
    n_claim = int(
        re.search(
            r'\d+',
            sess_html.select('h5')[0].text
        ).group()
    )

    is_logged = sess_html.select('p.userid')
    message = (
        f'{"ALREADY "*is_claimed}CLAIMED: {n_claim+(not is_claimed)}/{PERIOD_D.day} DAYS'
        if is_logged
        else 'ERROR: Wrong Login Credential'
    )

    return (not is_logged, message)


def login(session, username, password):
    data = {
        USER_NAME: username,
        PASS_NAME: password,
    }

    session.post(LOGIN_URL, data=data)


if __name__ == '__main__':
    os.system('cls')

    with open(PATH / 'data.json', 'r') as json_file:
        data = json.load(json_file)

    if len(arg := sys.argv) > 1 and re.match(r'^\d+$', arg[1]):
        num = arg[1]
    else:
        print('\n'.join(f'{str(i+1)+".":<3} {j.get("username")}' for i, j in enumerate(data)))

        num = input(f'Starting Point(1 - {len(data)}): ') or 1

        print()

    start = min(len(data), max(1, int(num)))-1

    main(data[start:])
