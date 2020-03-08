#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 定义集合
a = [1, 2, [3, 4], 5]

"""增加元素"""
a.append(6)

print(a)  # [1, 2, [3, 4], 5, 6]

"""两个空的集合是相等的"""
empty_list1 = []
empty_list2 = []
print(empty_list1 == empty_list2)  # True

"""可以直接加两个集合"""
language_java = ['java']
language_python = ['python']
language_all = language_java + language_python
print(language_all)  # ['java', 'python']

"""注意是不可以减的"""
# language_java_new = language_all - language_python
# print(language_java_new)


"""在指定位置插入"""
language_all.insert(1, 'c++')
print(language_all)  # ['java', 'c++', 'python']
