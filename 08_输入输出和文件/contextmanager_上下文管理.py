#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import contextmanager

"""
实现上下文自动管理，可以使用with的形式
"""


@contextmanager
def my_open(name: str):
    try:
        f = open(name, 'w')
        yield f  # 直接返回让外面用
    finally:
        f.close()


if __name__ == '__main__':
    with my_open('my_open.txt') as f:
        print(f)  # <_io.TextIOWrapper name='my_open.txt' mode='w' encoding='UTF-8'>
        f.write('new line\n')
        f.write('new line\n')
