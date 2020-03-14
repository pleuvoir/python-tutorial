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

# 判断列表是不是空
if not empty_list1:
    print('is empty')  # 为空
else:
    print('is not empty')

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

"""列表解析"""

list_old = [1, 2, 3, 4]  # 想要 [2,3,4,5]，普通方法是遍历，快速方法可以使用列表解析

list_new = [item + 1 for item in list_old]
print('list_new', list_new)  # [2, 3, 4, 5]

# 同时还可以做过滤
list_new = [item + 1 for item in list_old if item % 2 == 0]
print(list_new)  # [3, 5]  先执行右边的过滤，然后再执行左边的格式化+1
