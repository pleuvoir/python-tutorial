#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from collections import OrderedDict

dict = OrderedDict()
dict['name'] = 'pleuvoir'
dict['age'] = 18

print(dict)  # OrderedDict([('name', 'pleuvoir'), ('age', 18)])
print(dict.items())  # odict_items([('name', 'pleuvoir'), ('age', 18)])

# 将对象转为json字符串
json_load = json.dumps(dict, ensure_ascii=False)  # 注意这个参数不然中文不能正常显示
print(json_load)  # {"name": "pleuvoir", "age": 18}

# 再将字符串转为字典
new_dict = json.loads(json_load)
print(type(new_dict), new_dict)  # <class 'dict'> {'name': 'pleuvoir', 'age': 18}

# 再将字典强制转换为原始类型
new_ordered_dict = OrderedDict(new_dict)
print(new_ordered_dict)  # OrderedDict([('name', 'pleuvoir'), ('age', 18)])

print(dict == new_ordered_dict)  # true 只要内容相同就行，尽管一个是OrderedDict，一个是dict
print(dict is new_ordered_dict)  # False
