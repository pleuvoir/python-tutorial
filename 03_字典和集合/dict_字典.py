#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""这个字典dict特别像json，可以这么理解"""

dict_a = {
    'key1': 1,
    'key2': '2'
}

print(dict_a)  # {'key1': 1, 'key2': '2'}

print(dict_a.get('key1'))  # 没找到的话，返回None，推荐使用
print(dict_a['key1'])  # 如果没有的话会报错，不推荐使用

"""可以返回所有的key"""
keys = dict_a.keys()
print(keys)  # dict_keys(['key1', 'key2'])

"""可以返回所有的value"""
values = dict_a.values()
print(values)  # dict_values([1, '2'])

"""增加值，如果之前有这个key，那么重新设置值"""
dict_a['key3'] = 3
print(dict_a)  # {'key1': 1, 'key2': '2', 'key3': 3}

"""弹完以后就没了，弹没有的会报错"""
print(dict_a.pop('key1'))
print(dict_a)  # {'key2': '2', 'key3': 3}

"""可以直接转为元组"""

t = tuple(dict_a)
print(t)  # ('key2', 'key3')

"""字典解析，KEY=最左边的值，VALUE是最右边循环中的每一个内容"""

dict_list = {item: item for item in range(10)}
print(dict_list)  # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
