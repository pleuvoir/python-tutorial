#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def add(a: list):
    # a = a + [1]  #这样不会变
    a.append([2])  # 这样会变
    print(a)


list_b = [1, 2, 3]
add(list_b)
print(list_b)  # [1, 2, 3] 并不会变

"""全局变量"""
z = 1


def global_test(a):
    global z  # 表示要修改全局变量
    z += a


global_test(a=10)
print(z)  # 11

"""参数默认值"""


def default_value(a, b=3):
    pass
