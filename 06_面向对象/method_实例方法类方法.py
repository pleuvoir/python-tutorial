#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class User(object):

    def __init__(self, name):
        self.name = name

    def instance_function(self):
        print('这是最普通的实例方法', self.name)

    @classmethod
    def class_function(cls):  # 其实就是有个cls的入参
        print('这是一个类方法')
        cls.static_method()

    @staticmethod
    def static_method():
        print('这是一个静态方法')


if __name__ == '__main__':
    user = User('pleuvoir')
    user.instance_function()  # 实例方法

    user.class_function()  # 类方法，可以通过实例调用
    User.class_function()  # 类方法，也可以通过类名调用

    User.static_method()  # 静态方法，通过类名调用
