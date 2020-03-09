#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""这种的需要手动关闭"""
f = open('readme.txt', mode='w', encoding='utf-8')
f.write('第零行\n')
f.writelines(['第一行\n', '第二行\n', '第三行\n'])
f.close()

with open('readme.txt', mode='a', encoding='utf-8') as txt:  # 追加模式
    txt.write('追加哦\n')

"""写文件，如果没有的话则创建，重复执行会覆盖原来的内容"""
with open('readme.md', 'w', encoding='utf-8') as md:
    for item in range(5):
        print(item, file=md)  # 使用这种也可以

"""追加文件内容，注意这个a"""
with open('readme.md', 'a', encoding='utf-8') as md:
    for item in range(3):
        print(item, file=md)
