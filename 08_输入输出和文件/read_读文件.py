#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""读取readme.md文件，readlines可以将所有的内容一次读取到一个list中，如果文件过大不建议使用（不存在会报错）"""
with open('readme.md', 'r', encoding='utf-8') as md:
    for line in md.readlines():
        print(line, end='')

"""读取readme.md文件，md本身也是个可迭代的，所以直接遍历它可以得到每行的内容，
    并且可以做格式处理（注意：只能遍历一次，想移动指针可以使用seek）
    推荐使用
"""
need_read = []
with open('readme.md', 'r', encoding='utf-8') as md:
    for item in md:  # 一次读一行
        need_read.append(item.strip('\n'))
    md.seek(0)
    for item in md:  # 现在可以重新遍历这个迭代器对象了
        need_read.append(item.strip('\n'))

print(need_read)

"""读取二进制文件 bytes-like b代表二进制w代表write"""
with open('binary.ec', 'bw') as bw:
    for item in range(5):
        bw.write(bytes(item))  # 注意转换格式
