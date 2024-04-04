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
import platform
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).parent
SYSTEM = platform.system()

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
REWARD_ID = 'data-id'
REWARD_CLS = '.reward-star'
REWARD_PROD = 'data-period'


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
    n_threads = len(data) + 1 # min(n_cores * 2, len(data)+1)
    stop = []
    fails = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
        executor.submit(print_wait, stop)

        futures = [executor.submit(user_claim, user) for user in data]

        for future, user in zip(futures, data):
            username = user.get('username')
            username = re.sub(r'@.*', '', username).ljust(max_len)

            try:
                message = future.result()
            except Exception as e:
                message = 'ERROR: ' + str(e)
                fails += 1

            print(username, message)

        stop.append(0)

    print(str(fails) + ' failed attempt' + 's'*(fails > 1) if fails else 'SUCCEED!!!')


def print_wait(stop):
    for dot in itertools.cycle(['.', '..', '...']):
        if stop:
            break

        print(f'waiting{dot:<3}', end='\r')
        time.sleep(0.5)


def user_claim(user):
    username = user.get('username')
    password = user.get('password')
    server = user.get('server')

    session = requests.Session()
    is_logged = login(session, username, password)

    assert is_logged, 'Wrong Login Credential'

    html = session.get(EVENT_URL)
    sess_html = BeautifulSoup(
        html.text,
        'html.parser'
    )

    is_claimed = claim(session, sess_html, server)

    return check_claim(sess_html, is_claimed)


def claim(session, sess_html, server):
    reward = sess_html.select(REWARD_CLS)

    if not reward:
        return False
    
    item_id = reward[0].get(REWARD_ID)
    item_prod = reward[0].get(REWARD_PROD)

    result = session.post(CLAIM_URL, data={
        ITEM_POST: item_id,
        PROD_POST: item_prod,
        SRVR_POST: server,
    }).json()
    
    message = result.get('message')
    data = result.get('data')

    assert '[-102]' not in data, 'Wrong Server ID'
    assert 'invalid' not in data, 'Reward/Period Mismatch'

    return message == 'success'


def check_claim(sess_html, is_claimed):
    n_claim = int(
        re.search(
            r'\d+',
            sess_html.select('h5')[0].text
        ).group()
    )

    message = 'ALREADY '*(not is_claimed) + f'CLAIMED: {n_claim+is_claimed}/{PERIOD_D.day} DAYS'    

    return message


def login(session, username, password):
    data = {
        USER_NAME: username,
        PASS_NAME: password,
    }

    r = session.post(LOGIN_URL, data=data)

    return r.url.endswith('pembayaran.php')


if __name__ == '__main__':
    os.system('cls' if SYSTEM == 'Windows' else 'clear')

    with open(ROOT / 'data.json', 'r') as json_file:
        data = json.load(json_file)

    if len(arg := sys.argv) > 1 and re.match(r'^\d+$', arg[1]):
        num = arg[1]
    else:
        print(
            '\n'.join(
                str(i+1) + '. ' + j.get('username')
                for i, j in enumerate(data)
            )
        )

        num = input(f'Starting Point(1 - {len(data)}): ') or 1

        print()

    start = min(len(data), max(1, int(num)))-1

    main(data[start:])
