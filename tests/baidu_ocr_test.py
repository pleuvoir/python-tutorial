#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

import requests

AK = 'X0xlt5vmch3wGvHUbYZF2aTo111'
SK = 'pA9H7w2hl0F3sUGK9KC5LN9bdmdhzztQ111'


def get_token(ak, sk):
    # http://ai.baidu.com/docs#/Auth/top
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    params = {
        'grant_type': 'client_credentials',
        'client_id': ak,
        'client_secret': sk,
    }
    r = requests.post(url, params=params)
    return r.json()['access_token']


TOKEN = get_token(AK, SK)

print(TOKEN)


def ocr(img_url):
    img_bytes = requests.get(img_url).content
    # https://ai.baidu.com/docs#/OCR-API/e1bd77f3
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
    params = {'access_token': TOKEN}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    img = base64.b64encode(img_bytes)
    data = {'image': img}
    r = requests.post(url, data=data, params=params, headers=headers)
    # 该项目只需要一个词
    print(r.json())  # {'log_id': 8146374314688758727, 'words_result_num': 0, 'words_result': []}
    return r.json()['words_result'][0]['words']


if __name__ == '__main__':
    IMAGE_URL = 'https://b2c.csair.com/ita/rest/intl/captcha/challenge?type=ac&_=1586253162424'
    ocr(IMAGE_URL)