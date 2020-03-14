#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class House(object):

    def __init__(self, title: str, price: str, desc: str):
        self._title = title
        self._price = price;
        self._desc = desc

    def toString(self) -> str:
        return '{} 价格 {} 描述 {}'.format(self._title, self._price, self._desc)
