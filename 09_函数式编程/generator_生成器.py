#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def my_range(total):
    value = 0
    while value < total:
        yield value  # 你可以把它理解为return，但是return只会返回一次，它会返回很多次，并且可以供你遍历
        value += 1


i = my_range(100)
print(i)  # 返回的就是一个生成器 <generator object my_range at 0x118cedd60>
print(dir(i))  # 可以发现里面有__iter__方法

# 注意只能使用一次
for item in i:
    print(item)  # 0
    break

for item in i:
    print(item)  # 1
    break
