#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""这个没啥说的，就是没有重复值"""

set1 = {1, 2, 3, 3}

print(set1)  # {1, 2, 3}
set1.add(3)
print(set1)  # {1, 2, 3}
set1.add(4)
print(set1)  # {1, 2, 3}

"""可以直接把list转成set，去掉重复值"""
list_value = [1, 2, 3, 3]
s = set(list_value)
print(s)  # {1, 2, 3}
