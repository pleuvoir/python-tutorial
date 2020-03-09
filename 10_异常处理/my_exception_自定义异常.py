#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MyException(Exception):
    pass


if __name__ == '__main__':
    try:
        raise MyException
    except Exception as e:
        if isinstance(e, MyException):
            print('是自定义异常')
    else:
        print('退出了')  # 没有异常这行会打印
    finally:
        print('我是finally的语句')
