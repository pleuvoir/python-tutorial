#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import OrderedDict

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
