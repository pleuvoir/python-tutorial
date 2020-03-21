#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import OrderedDict
from collections import namedtuple

# 有序的字典
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

for k, v in enumerate(ordered_dict):
    print(k, v)

items = ordered_dict.items()
for k, v in items:
    print(k, v)

# 带有命名的tuple，提高可读性

student = namedtuple('Student', 'name,id')

students = [
    student('pleuvoir', 1),
    student('abama', 2)
]

for student in students:
    print('name={}，id={}'.format(student.name, student.id))
    print('name={}，id={}'.format(student[0], student[1]))
