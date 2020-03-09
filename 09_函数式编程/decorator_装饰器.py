#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools


# 第一步


def origin(x):
    print(x)


def origin_aop(f):
    def f_new(x):
        function_name = f.__name__
        print(f'目标函数{function_name}调用前')
        result = f(x)
        print(f'目标函数{function_name}调用后')
        return result

    return f_new


# 进行增强，这里是对函数进行增强，不是直接调用，所以没有传参不要奇怪
# aop = origin_aop(origin)
# aop(2)

"""输出结果：
目标函数origin调用前
2
目标函数origin调用后
"""


# 第二步：使用装饰器，可以认为上面定义的高阶函数就自动支持这个装饰器了，缺陷只能传递一个参数

@origin_aop
def target_func(x):
    print(x)


# target_func(1)
"""输出结果：
目标函数target_func调用前
1
目标函数target_func调用后
"""


# 第三步：优化为多参数

def origin_aop_better(f):
    def f_new_better(*args, **kwargs):
        function_name = f.__name__
        print(f'目标函数{function_name}调用前')
        result = f(*args, **kwargs)
        print(f'目标函数{function_name}调用后')
        return result

    return f_new_better


@origin_aop_better
def target_func_better(*args, **kwargs):
    print(args)
    print(kwargs)


# target_func_better(1, 2, 3, x=4, y=5)

#  第四步：带参数的装饰器，这个就像俄罗斯套娃一样（这里需要使用一个内置库解决加了装饰器后名字和注释不正确的问题）

def origin_aop_better_with_args(s):
    def more(f):
        @functools.wraps(f)  # copy一些属性过来解决__name__和__doc__不正确的问题
        def f_new_better(*args, **kwargs):
            print('装饰器传进的参数是{0:>20}'.format(s))
            function_name = f.__name__
            print(f'目标函数{function_name}调用前')
            result = f(*args, **kwargs)
            print(f'目标函数{function_name}调用后')
            return result

        return f_new_better  # 这个东西本来就是个装饰器，上一步已经使用过了

    return more


@origin_aop_better_with_args('hello，我是装饰器的参数')
def target_func_better_with_args(*args, **kwargs):
    """

    :param args: 装饰器的参数
    :param kwargs: 装饰器的参数
    :return:
    """
    print(args)
    print(kwargs)


# target_func_better_with_args(1, 2, 3, x=4, y=5)
print(target_func_better_with_args.__name__)  # 如果没加functools 则显示的不正确 f_new_better
print(target_func_better_with_args.__doc__)  # 如果没加functools 则显示的不正确 None
