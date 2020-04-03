#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pip install APScheduler
具体参考：https://www.jianshu.com/p/ad2c42245906
"""

import datetime
import time

from apscheduler.schedulers.background import BackgroundScheduler


def do_job():
    print('任务执行时间：{}'.format(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]))

if __name__ == '__main__':
    # 创建后台执行的 schedulers
    scheduler = BackgroundScheduler()
    # 添加调度任务
    # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 2 秒
    scheduler.add_job(do_job, 'interval', seconds=2)
    # 启动调度任务
    scheduler.start()

    while True:
        time.sleep(5)