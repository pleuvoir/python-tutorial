#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pynput.keyboard import Key

from tests.pyinput_helper import *

helper = OptHelper()


def _open_logined_tab():
    helper.comb(Key.cmd, singe_key='t')
    helper.input('ssh KG')
    helper.press(Key.enter)


if __name__ == '__main__':
    # 先打开 iterm 正常登陆跳板机，并设置为最大窗口，注意输入法为英文
    # 打开 iterm
    helper.position((1200, 1000))
    helper.left_click()

    _open_logined_tab()

    # 关掉其它的 tab
    helper.position((50, 10))
    helper.right_click()
    helper.position((100, 100))
    helper.left_click()
