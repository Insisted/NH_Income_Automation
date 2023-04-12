"""
Ninja Heroes: New Era

Script to claim Ninja Income for those who have many accounts
Will only supporting `Chrome`, `Edge`, and `Firefox` on `Windows` only presumably
The script will run on your browser's private/incognito mode, except for `Firefox`
"""

import json
import re
import sys
import time

import requests
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import (Chrome, ChromeOptions, Edge, EdgeOptions,
                                Firefox, FirefoxOptions)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from webdriver_manager import chrome, firefox, microsoft


CONFIG_DETAIL = {
    'chrome': {
        'options': ChromeOptions,
        'arguments': '-incognito',
        'driver': Chrome,
        'driver_manager': chrome.ChromeDriverManager
    },
    'edge': {
        'options': EdgeOptions,
        'arguments': '-inprivate',
        'driver': Edge,
        'driver_manager': microsoft.EdgeChromiumDriverManager
    },
    'firefox': {
        'options': FirefoxOptions,
        'arguments': '--start-maximized',
        'driver': Firefox,
        'driver_manager': firefox.GeckoDriverManager
    }
}

BROWSER = 'Chrome'
LOGIN_URL = 'https://www.kageherostudio.com/payment/login.php'
CLAIM_URL = 'https://www.kageherostudio.com/event/?event=daily'


def main(data, num):
    start = data[num:]
    max_data = max(
        start,
        key=lambda x: (y := re.match(
            r'^.*(?=@)', x.get('username')).span())[1] - y[0]
    )
    max_len = len(
        re.sub(r'@.*', '', max_data.get('username'))
    )

    # FIXME: Firefox can run on incognito mode but it can't print the proper days
    #        on `print_claimed` (cookies related), now its argument is `--start-maximized`
    browser_options = config.get('options')()

    if config.get('arguments') in ('-incognito', '-inprivate'):
        # Simple check, only for Chrome and Edge.
        browser_options.add_argument(config.get('arguments'))
        browser_options.add_experimental_option(
            'excludeSwitches',
            ['enable-logging']
        )

    driver = config.get('driver')(
        options=browser_options,
        service=Service(
            executable_path=config.get('driver_manager')(
                path=r'.\driver'
            ).install()
        )
    )

    for n, user in enumerate(start):
        _username = user.get('username')
        _password = user.get('password')
        _server = user.get('server')

        print(f'{str(n+num+1)+".":<3} {re.sub(r"@.*", "", _username):<{max_len}}', end='')

        driver.get(LOGIN_URL)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, 'topup-form-btnSubmit')
            )
        )

        username_input = driver.find_element(by=By.NAME, value='txtuserid')
        password_input = driver.find_element(by=By.NAME, value='txtpassword')

        username_input.send_keys(_username)
        password_input.send_keys(_password)

        submit = driver.find_element(by=By.ID, value='topup-form-btnSubmit')
        submit.click()

        driver.get(CLAIM_URL)

        try:
            fa_star = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, 'fa-star')
                )
            )

        except TimeoutException:
            print_claimed(driver)
            continue

        fa_star.click()
        time.sleep(1)

        dropdown = Select(driver.find_element(by=By.NAME, value='selserver'))
        dropdown.select_by_value(str(_server))

        submit = driver.find_element(by=By.ID, value='form-server-btnSubmit')
        submit.click()

        driver.switch_to.alert.accept()

        print_claimed(driver)
        time.sleep(1)

    else:
        print('SUCCEED!!!')

    driver.close()


def print_claimed(driver):
    cookie = driver.get_cookie('PHPSESSID') or {'name': '', 'value': ''}

    session = requests.Session()
    session.cookies.set(cookie['name'], cookie['value'])

    sauce = session.get(CLAIM_URL)
    claimed = BeautifulSoup(
        sauce.text,
        'html.parser'
    ).select('h5')[0].text.replace('LOGIN COUNT ', '')

    print(' CLAIMED' + claimed)


if __name__ == '__main__':
    config = CONFIG_DETAIL[
        (
            arg[1] if len(arg := sys.argv) > 1 and arg[1].lower() in CONFIG_DETAIL.keys()
            else BROWSER
        ).lower()
    ]

    with open(r'.\data.json', 'r') as json_file:
        data = json.load(json_file)

    print('\n'.join(f'{str(i+1)+".":<3} {j.get("username")}' for i, j in enumerate(data)))

    num = input(f'Starting Point(1 - {len(data)}): ')
    print()

    main(data, min(len(data), max(1, int(num)))-1)
