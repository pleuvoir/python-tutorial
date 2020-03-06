#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print函数
print('hello world')

# 键盘输入
name = input("what's your name?")
print(name)  # 打印出你输入的值

# 判断对象类型
t_a = 1
t_b = 'hello'

print(type(t_a))  # <class 'int'>
print(type(t_b))  # <class 'str'>

# 数学运算，注意//会丢失精度
a = 16;
b = 4;
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # float类 4.0
print(a // b)  # 4
print(a % b)  # 0
print(a + a / b)  # 20.0
print(a + a // b)  # 20
print(a + b / a)  # 16.25
print(a + b // a)  # 16  会丢失精度


