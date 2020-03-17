#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" pip install retrying"""

import random

from retrying import retry


@retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=5000)
def test():
    print(random.randint(0, 2))
    raise RuntimeError('出错了')


if __name__ == '__main__':
    try:
        test()
    except RuntimeError as exc:
        print(exc.args)


class HttpRequestException(Exception):
    pass