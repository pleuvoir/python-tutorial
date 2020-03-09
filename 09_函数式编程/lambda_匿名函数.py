#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 定义匿名函数
f = lambda x, y: x + y * 2


def test(a, b):
    return f(x=a, y=b)


print(f(1, 2))
print(test(1, 2))
