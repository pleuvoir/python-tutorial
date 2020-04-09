#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time

#  键盘操作
from pynput.keyboard import Controller as keyboardC
# 鼠标操作
from pynput.mouse import Controller as mouseC, Button


class OptHelper(object):

    def __init__(self):
        self.mouse = mouseC()
        self.keyboard = keyboardC()

    def get(self):
        return self.mouse, self.keyboard

    def position(self, position):
        self.mouse.position = position
        time.sleep(1)

    def press(self, key):
        self.keyboard.press(key)
        self.keyboard.release(key)

    def comb(self, *args, singe_key):
        with self.keyboard.pressed(*args):
            self.keyboard.press(singe_key)
            self.keyboard.release(singe_key)

    def input(self, text):
        self.keyboard.type(text)
        time.sleep(1)

    def left_click(self):
        self.mouse.click(Button.left, 1)
        time.sleep(1)

    def right_click(self):
        self.mouse.click(Button.right, 1)
        time.sleep(1)
