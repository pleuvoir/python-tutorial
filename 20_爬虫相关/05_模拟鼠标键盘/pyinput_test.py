#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pip3 install pynput
这个库让你可以控制和监控输入设备。
对于每一种输入设备，它包含一个子包来控制和监控该种输入设备：
pynput.mouse：包含控制和监控鼠标或者触摸板的类。
pynput.keyboard：包含控制和监控键盘的类。
"""

import time

#  键盘操作
from pynput.keyboard import Controller as keyboard, Key
# 鼠标操作
from pynput.mouse import Controller as mouse, Button

mouse = mouse()
keyboard = keyboard()


def open_terminal():
    # 移动到 iterm的位置，点击左键
    print('当前鼠标位置 {0}'.format(mouse.position))
    mouse.position = (1180, 1000)
    print('现在我们移动到了 {0}'.format(mouse.position))
    mouse.click(Button.left, 1)
    time.sleep(1)


def open_logined_tabs(num: int):
    """
    打开几个tab
    """
    for _ in range(num):
        _open_logined_tab()


def _open_logined_tab():
    with keyboard.pressed(Key.cmd):
        keyboard.press('t')
        keyboard.release('t')
        time.sleep(1)
    keyboard.type('ssh KG')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)


def open_invoice_server():
    # 先关闭其他tab
    mouse.position = (50, 10)
    time.sleep(1)
    mouse.click(Button.right, 1)
    time.sleep(1)
    mouse.position = (100, 100)
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    exit(-1)
    print('打开发票服务所有机器，并进入日志目录')
    ip_list = ['88.88.9.150', '88.88.9.151']
    for ip in ip_list:
        _open_logined_tab()  # 打开新tab
        keyboard.type(ip)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.type('cd /opt/dsf/log/invoice_server/')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.type('ls')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(1)


if __name__ == '__main__':
    # 先打开 iterm 正常登陆跳板机，并设置为最大窗口，注意输入法为英文
    open_terminal()
    open_invoice_server()
