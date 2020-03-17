#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools
import random
import threading
import time
from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor


def runnable(name):
    _sleep_sec = random.randint(1, 5)
    time.sleep(_sleep_sec)
    print('当前线程{}准备休息{}s，name={}'.format(threading.current_thread().getName(), _sleep_sec, name))
    return _sleep_sec


def call_back(future: Future):
    print(f'我能获取到Future的结果{future.result()}')


def enhance_call_back(future: Future, **kwargs):
    print(f'我能获取到Future的结果{future.result()}，还有其它参数{kwargs}')


if __name__ == '__main__':
    max_worker = 5
    # with ThreadPoolExecutor(max_workers=max_worker, thread_name_prefix='test-') as executor:
    #     future_list = []
    #     for item in range(max_worker):
    #         future = executor.submit(runnable, name='pleuvoir')
    #         future_list.append(future)
    #     for future in future_list:
    #         try:
    #             result = future.result(timeout=1)
    #         except Exception as exc:
    #             if isinstance(exc, concurrent.futures._base.TimeoutError):
    #                 print('出现超时异常了')
    #         else:
    #             print('没有异常')

    with ThreadPoolExecutor(max_workers=max_worker, thread_name_prefix='test-') as executor:
        for index in range(max_worker):
            f = executor.submit(runnable, name='pleuvoir')
            # f.add_done_callback(call_back)

            # 由于add_done_callback只能接受一个参数，所以增强一下
            partial = functools.partial(enhance_call_back, name='pleuvoir', age=18)
            f.add_done_callback(partial)
