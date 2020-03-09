#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Hero(metaclass=ABCMeta):  # 代表这是一个抽象类

    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    @abstractmethod
    def say(self):
        pass

    def opt(self):
        print('我是{}，我会使用技能{}'.format(self.name, self.skill))


class AD(Hero):

    def __init__(self, name, skill):
        super().__init__(name, skill)

    def say(self):
        print('我说什么好呢，我是重写的')


if __name__ == '__main__':
    ad = AD('盖伦', '正义审判')
    ad.say()
