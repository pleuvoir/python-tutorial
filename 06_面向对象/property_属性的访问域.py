#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
面向对象展示类
如果属性或者方法以单下划线_开头，则为protected，其他类不建议访问，因为是内部属性随时可能删除
如果属性或者方法以双下划线__开头，则调用会报错
"""

from datetime import datetime


class Account(object):
    # 类属性
    count = 0

    def __init__(self, name: str, balance=0):
        Account.count += 1  # 每次都会+1，可以统计这个类实例化了多少次
        self.name = name
        self.balance = balance
        self.__history = []  # 交易记录私有的属性，只能通过方法访问
        self._args = []  # 定义访问属性，只在类中可以访问

    def recharge(self, amount):
        self.balance + amount
        self.__history.append('{}：充值{}元'.format(Account._current_time(), amount))  # 注意静态方法使用 类名.方法名 的形式调用
        self._args.append(amount)

    """加了这个注解以后就可以不用括号进行访问了"""

    @property
    def history(self):
        return self.__history

    @history.setter
    def history(self, history):
        self.__history = history

    """静态方法"""

    @staticmethod
    def _current_time():
        return datetime.now()

    def show_history(self):
        for item in self.__history:
            print(item)


if __name__ == '__main__':
    account = Account('pleuvoir')
    account.recharge(10)
    account.show_history()
    # 获取历史
    history = account.history  # 因为@property的存在 account.history()会报错了
    print(history)

    # 设置历史
    account.history = [1, 2, 3]
    print(account.history)  # [1, 2, 3]
