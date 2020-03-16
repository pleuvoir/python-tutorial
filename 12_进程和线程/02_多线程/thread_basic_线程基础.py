#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time

# 以列表形式返回当前所有存活的线程，包含守护线程
threading_enumerate = threading.enumerate()
print(threading_enumerate)

# 线程本地数据
threading_local = threading.local()
threading_local.x = 'pleuvoir'
print(threading_local.x)  # pleuvoir

# 创建一个线程

"""我们先定义一个需要执行的方法"""


def runable(name):
    for item in range(10):
        print('当前线程名称{}，输出{}{}'.format(threading.current_thread().getName(), name, item))
        time.sleep(1)


t = threading.Thread(name='test-name', target=runable, args=('pleuvoir',))  # 注意这个,很关键，没有就报错了
# t.setDaemon(True)
t.start()

t.join()  # t线程插队到当前线程之前运行

print('当前线程名称{}，输出{}'.format(threading.current_thread().getName(), t.getName()))
