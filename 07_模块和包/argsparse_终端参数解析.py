#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys

"""
1. 比如我们要实现一个-p 1 或者--print 1 打印出1的功能
2. 在上述功能的基础上接收多个参数，也就是一次执行好几个功能 
        -p 1 -a -1  
        -p 1 -abs -1
        打印出1 并且打印出-1的绝对值
"""

if __name__ == '__main__':

    print(sys.argv)  # 这是命令行接收到的参数返回的是list，index=0是文件名称

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--print", help="输出你传入的值")
    parser.add_argument("-a", "--abs", type=int, help="输出你传入值的绝对值，只能为int")
    args = parser.parse_args()

    # 如果指定了长短参，必须使用长参数来获取值
    if args.print:
        print(args.print)
    if args.abs:
        print(abs(args.abs))
