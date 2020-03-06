#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# !/usr/bin/env python3

# -*- coding: utf-8 -*-


# 多参数，不能指定关键字，类似元组
def mutil_args(*args):
    for arg in args:
        print(arg)


# 多参数，可以指定关键字，类似字典
def test2(**kwargs):
    print(kwargs)


#  **kwargs的优点，如果test方法发生改变，这个函数不需要变动；
#  所以可以这么理解，如果对外暴露的函数里面调用了其他容易变动的函数，可以使用这个避免对外接口频繁改变
def add(value, **kwargs):
    if value == 1:
        test(**kwargs)  # 特别注意，这里传递的要带 ** 号


def test(a, b, c):
    print(a + b)


if __name__ == '__main__':
    # mutil_args(1, 2, 3)
    add(value=1, a=2, b=3, c=4)
