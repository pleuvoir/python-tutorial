#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

if __name__ == '__main__':
    """从网络上读取"""
    IMAGE_URL = 'https://b2c.csair.com/ita/rest/intl/captcha/challenge?type=ac&_=1586253162424'

    r = requests.get(IMAGE_URL)
    print(r.content,'\n',type(r.content))  #bytes
    # with open('img2.png', 'wb') as f:
    #     f.write(r.content)
