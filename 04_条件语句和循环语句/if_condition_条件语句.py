#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 这个和java的差不多  not就是！ and就是&& or 是||

"""年龄"""
print("输入你的年龄：")
age = int(input())
if age < 18 or age >= 65:
    print("回家歇着")
else:
    print("好好搬砖")


"""去游泳"""
day = "Monday"
temperature = 30
raining = False

if day == "Monday" and temperature > 25 and not raining:
    print("去游泳")
else:
    print("在家学习")


"""同时它还有elseif"""

name = 'pleuvoir'
if name == 'pleuvoir':
    pass
elif name == 'java':
    pass
else:
    pass
