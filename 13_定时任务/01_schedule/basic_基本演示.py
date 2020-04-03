#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pip install schedule

这个是基于内存实现的，如果想看详细的可以参考https://www.jianshu.com/p/57d09d3c8998
"""
import datetime
import time

import schedule


# 定义你要周期运行的函数
def do_job():
    print('任务执行时间：{}'.format(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]))


schedule.every(10).minutes.do(do_job)  # 每隔 10 分钟运行一次 job 函数
schedule.every().hour.do(do_job)  # 每隔 1 小时运行一次 job 函数
schedule.every().day.at("10:30").do(do_job)  # 每天在 10:30 时间点运行 job 函数
schedule.every().monday.do(do_job)  # 每周一 运行一次 job 函数
schedule.every().wednesday.at("13:15").do(do_job)  # 每周三 13：15 时间点运行 job 函数
schedule.every().minute.at(":17").do(do_job)  # 每分钟的 17 秒时间点运行 job 函数

while True:
    schedule.run_pending()  # 运行所有可以运行的任务
    time.sleep(1)
