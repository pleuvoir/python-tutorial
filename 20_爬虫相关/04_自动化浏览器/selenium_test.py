#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from selenium import webdriver


def _get_orders():
    with open('orders.txt', 'r') as r:
        return [line.strip() for line in r.readlines()]


if __name__ == '__main__':
    browser = webdriver.Chrome(executable_path='./chromedriver')

    browser.get('https://suyun-developer.daojia-inc.com/#/')
    browser.maximize_window()
    browser.implicitly_wait(6)

    userName = browser.find_element_by_id('userName')
    userName.send_keys('inpass 账号')

    password = browser.find_element_by_id('password')
    password.send_keys('inpass 密码')

    # # input_search.submit() #这样也可以，只要它和提交按钮在一个 form 里

    su_button = browser.find_element_by_id('btnSubmit')
    su_button.click()



    orders = _get_orders()

    root_folder = os.getcwd()
    screen_folder = os.path.join(root_folder, 'screens')
    os.chdir(os.path.join(os.getcwd(), 'screens'))

    for order_id in orders:
        order_page = browser.get(
            f'https://suyun-settle.daojia-inc.com/suyuntradeManager/tradeInfo?orderId={order_id}')

        try:
            browser.get_screenshot_as_file(f'{screen_folder}/{order_id}.png')
            print('{} 截图成功'.format(order_id))
        except BaseException as msg:
            print(msg)

    browser.quit()
