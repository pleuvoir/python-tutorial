#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 如果不带括号的这种写法，其实它本质上就是元组
var_a = 1, 2
var_b = (1, 2)
print(var_a is var_b)  # True
print(var_a == var_b)  # True

"""元组的特点是不可以修改，但是不代表里面的元素不可变，比如其中一个元素是list"""

var_unmodify = (1, 2, [3, 4])
modify_list = var_unmodify[2]
modify_list.append(5)

print(var_unmodify)  # (1, 2, [3, 4, 5])

"""也可以通过值来找索引，没找到会报错"""
print(var_unmodify.index(2))
