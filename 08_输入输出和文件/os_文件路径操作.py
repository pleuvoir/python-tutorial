#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# 获取当前的路径
print(os.getcwd())  # /Users/pleuvoir/dev/space/git/python-tutorial/08_输入输出和文件

# 获取当前文件夹下的文件
print(os.listdir())  # ['os_文件路径操作.py', 'write_写文件.py', 'readme.md', 'readme.txt', 'read_读文件.py']

# 如果没有folder文件夹则创建文件夹
if not os.path.exists('folder'):
    os.mkdir('folder')
else:
    print('已经存在文件夹，不再创建')

# 判断是否文件夹
print(os.path.isdir('folder'))  # True

# 切换到该文件夹下
os.chdir('folder')
print(os.listdir())

# 拼接路径的方法，不用 + 去拼接了 非常好
# /Users/pleuvoir/dev/space/git/python-tutorial/08_输入输出和文件/folder/test/test2
print(os.path.join(os.getcwd(), 'test', 'test2'))
