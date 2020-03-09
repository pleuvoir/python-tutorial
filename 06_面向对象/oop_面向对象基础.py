#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""普通的面向对象"""


class Hero(object):

    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def opt(self):
        print('我是{}，我会使用{}'.format(self.name, self.skill))


"""继承"""


class AD(Hero):

    def opt(self):  # 可以重写
        super().opt()
        print('已经重写')


if __name__ == '__main__':
    gaylon = Hero('盖伦', '沉默')
    gaylon.opt()

    ad = AD('寒冰', '魔法水晶剑')
    ad.opt()
