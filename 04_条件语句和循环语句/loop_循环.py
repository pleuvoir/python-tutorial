#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""常规的都可以循环，尝试在下面输入iter看有什么提示，一般都会生成表达式"""
var_a = 1, 2, 3

for item in var_a:
    print(item)

l = list(var_a)
for item in l:
    print(item)

dict_value = {
    'name': 'pleuvoir',
    'age': 18
}

for k, v in dict_value.items():  # 打印字典的
    print(k, v)

"""中断的循环可以额外打一行字"""

array = 1, 2, 3

for item in array:
    if item == 2:
        print('我是2，break了。')
        break
else:
    print('只要不break，循环结束后我会执行')

# While循环

"""这里注意，和for循环一样只要不是break的 一样会最终输出else里的内容"""
count = 0
while True and count <= 10:
    print('我一直是真')
    count += 1
    # if count >= 10:
    #     break
else:
    print('结束了')
