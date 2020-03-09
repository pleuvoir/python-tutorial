#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import path

if '/Users/pleuvoir/dev/space/git/python-tutorial' not in path:
    path.append('/Users/pleuvoir/dev/space/git/python-tutorial')

"""它打出来的是一个list，如果你使用的是ide，它会自己把当前目录加进去，会导致如果你在命令行下执行，可能会出现找不到该模块"""
print(path)  # '/Users/pleuvoir/dev/space/git/python-tutorial/07_模块和包', '/Users/pleuvoir/dev/space/git/python-tutorial'

"""使用 https://pypi.org/ 进行包的搜索"""
