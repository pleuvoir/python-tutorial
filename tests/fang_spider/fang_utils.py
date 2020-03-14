#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os

import requests

log = logging.getLogger(name='fang_spider')
log_format = '%(levelname)s-%(asctime)s-%(threadName)s-%(name)s-%(message)s'
logging.basicConfig(level='INFO', format=log_format)

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:73.0) Gecko/20100101 Firefox/73.0'}

INDEX_PAGE_MOCK = 'https://xian.newhouse.fang.com/house/s/gaoxin11/b9{}-c23/'

PAGE_SIZE = 20


def save_html(filename: str, text: str):
    """
    保存抓取到的详情页面，方便查看
    :param filename: 文件名称
    :param text:  文件内容
    :return:
    """
    folder = os.path.join(os.getcwd(), 'fang_details')
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(f'{folder}/{filename}.html', 'w') as f:
        print(text, file=f)


def save_comment_by_userid(filename: str, text: str):
    folder = os.path.join(os.path.dirname(__file__), 'fang_user_comments')
    if not os.path.exists(folder):
        os.mkdir(folder)
    # 如果文件不存在则创建
    with open(f'{folder}/{filename}.txt', 'a') as f:
        print(text, file=f)


def go(url: str, **kwargs):
    """
    请求房天下的地址，进行了自动转码
    :param url: 请求地址
    :return: 文本
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=5, params=kwargs.get('params'))
        # 用gbk转码，否则是乱码
        text = response.text.encode(response.encoding).decode('gbk')
        return text
    except Exception as e:
        warn('请求 {} 失败，{}'.format(url), e)
        return ''


def post(url: str, data: dict):
    response = requests.post(url,
                             headers=HEADERS,
                             data=data,
                             timeout=30)
    text = response.text.encode(response.encoding).decode('gbk')
    return text;


def post_tryable(url: str, data: dict, max_times=3):
    _current_times = 1
    while _current_times <= max_times:
        text = post(url=url, data=data)
        _current_times += 1
        if not text == '':
            return text


def go_tryable(url: str, max_times=3, **kwargs):
    _current_times = 1
    while _current_times <= max_times:
        text = go(url=url, **kwargs)
        _current_times += 1
        if not text == '':
            return text


def list2str(xpath_list: list):
    """
    因为xpath返回有时是个list，所以需要转为str，并且过滤掉空内容
    :param list: xpath返回的list
    :return: 格式化后的文本
    """
    return ''.join(xpath_list).strip('\t\n ')


def get_page_size(record_total: str):
    """
    获取共有多少页，目前房天下每页显示20条
    :param record_total: 共有多少记录
    :return: 共有几页
    """
    total_split = str(int(record_total) / PAGE_SIZE).split('.')
    if total_split[1] == '0':
        return int(total_split[0])
    else:
        return int(total_split[0]) + 1


def info(message: str):
    log.info(message)


def error(message: str):
    log.error(message)


def warn(message: str):
    log.warning(message)
