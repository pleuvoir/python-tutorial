#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""房天下爬虫"""

import json
import shutil
from collections import OrderedDict

from lxml import etree

from tests.fang_spider.fang_utils import *
from tests.fang_spider.house import House

house_list = []


def start():
    # 1.判断高新区三居室新房有多少条
    page_size = _get_page_size()
    info('当前高新区三居室新房共有{}页'.format(page_size))
    # 2.开始循环抓取首页
    for current_page in range(1, page_size + 1):
        text = go_tryable(INDEX_PAGE_MOCK.format(current_page))  # 当前首页的内容
        html = etree.HTML(text)  # 使用xpath解析
        a_from_title = html.xpath('//div[@class="nlcd_name"]/a')  # 找到首页下标题对应的所有的a连接
        for a in a_from_title:  # 开始循环进入详情页
            _title = list2str(a.xpath('text()'))
            domain = list2str(a.xpath('@href'))
            _href = f'https:{domain}'
            log.info('标题：{} 链接：{}'.format(_title, _href))
            _get_detail(title=_title, href=_href)
            # 3.开始抓取点评
            _get_dianping(title=_title, detail_url=_href)


def _get_dianping(title: str, detail_url: str):
    # 获取这个详情页面的内容
    text = go_tryable(detail_url)
    html = etree.HTML(text)
    # 获取房屋id，可以从楼盘详情链接中得到
    href = list2str(html.xpath('//meta[@name="mobile-agent"]/@content'))
    house_id = href.split('/')[5].strip('.htm')
    _dianping_url = f'{detail_url}/house/ajaxrequest/dianpingList_201501.php'
    log.info('开始抓取点评，标题：{} 点评AJAX链接：{}，house_id={}'.format(title, _dianping_url, house_id))
    # 请求ajax获取评论信息，这里取个巧，直接获取总数，然后把pagesize改为这个总数，这样就一次性获取到了
    text = post_tryable(_dianping_url,
                        {'city': '西安', 'dianpingNewcode': house_id, 'ifjiajing': 0, 'tid': '', 'page': 1, 'pagesize': 1,
                         'starnum': 0,
                         'shtag': -1, 'rand': 0.8865550224456968, })
    count = json.loads(text).get('count')
    log.info('开始抓取点评，标题：{} ，house_id={}，评论数={}，开始抓取所有评论'.format(title, house_id, count))
    # 获取所有的评论，并写入文件
    all_comment = post(_dianping_url,
                       {'city': '西安', 'dianpingNewcode': house_id, 'ifjiajing': 0, 'tid': '', 'page': 1,
                        'pagesize': count,
                        'starnum': 0,
                        'shtag': -1, 'rand': 0.8865550224456968, })
    comment_list = json.loads(all_comment).get('list')
    write_usage_list = []
    for comment in comment_list:
        # 组装写入文件每行的内容
        formated_comment = ''.join(comment.get('content').replace('<br/>', '').replace('\n', '').split())

        write_usage = '[{0}]|[{1}]|[{2}]|{3}\n'.format(comment.get('user_id'), comment.get('username'),
                                                       comment.get('create_time'),
                                                       formated_comment)
        write_usage_list.append(write_usage)

    folder = os.path.join(os.getcwd(), 'fang_comments')
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(f'{folder}/{title}_[评论{count}条].txt', 'w') as f:
        f.writelines(write_usage_list)


def _get_page_size():
    """
    获取当前条件查询下共有多少页，方便遍历查询
    :return: 分页数目
    """
    # 第一页的内容
    text = go_tryable(INDEX_PAGE_MOCK.format(1))
    # 获取分页位置显示的页数
    html = etree.HTML(text)  # 使用xpath解析
    record_total = list2str(html.xpath('//div[@id="sjina_C01_47"]/ul/li/b/text()'))
    page_size = get_page_size(record_total)  # 共有这么多页
    return page_size;


def _get_detail(title: str, href: str):
    # 获取这个详情页面的内容
    text = go_tryable(href)
    # 获取均价
    html = etree.HTML(text)
    price = list2str(html.xpath('//span[@class="prib cn_ff"]/text()'))
    if not price:
        # 如果没有获取到，则换个方式
        price = list2str(html.xpath('//div[@class="l-price"]/strong/text()'))
    # 获取信息
    ele = html.xpath('//div[@class="mb20 clearfix"]/div')
    house_info = OrderedDict()
    for cell in ele:
        _title = list2str(cell.xpath('div/h1/text()'))
        _content = list2str(cell.xpath('div/p/text()'))
        house_info[_title] = _content

    house = House(title=title, price=price, desc=json.dumps(house_info, ensure_ascii=False))
    house_list.append(house)


if __name__ == '__main__':
    # start()

    with open('result.txt', 'w') as f:
        for i, h in enumerate(house_list):
            print('{}.{}'.format(i + 1, h.toString()), end='\n\n', file=f)

    info('当前高新区三居室新房抓取结束')

    info('开始分析用户')

    # 评论文件夹
    folder = os.path.join(os.getcwd(), 'fang_comments')
    os.chdir(folder)
    comment_txt = os.listdir()

    #  强制清空单个用户评论文件夹
    user_comments_folder = os.path.join(os.path.dirname(__file__), 'fang_user_comments')
    shutil.rmtree(user_comments_folder)

    # 记录用户评论的次数
    all_user_comment_counter = {}

    txt_name_list = [txt_name for txt_name in comment_txt if
                     not os.path.isdir(txt_name) and os.path.splitext(txt_name)[1] == '.txt']  # 过滤掉目录
    for txt_name in txt_name_list:
        house_name = txt_name.split('_')[0]
        with open(os.path.join(folder, txt_name), 'r', encoding='utf-8') as f:
            # 一次读一行，并根据用户id创建评论文件
            for line in f:
                line_split = line.split('|')
                user_id = line_split[0]
                user_name = line_split[1]
                comment = line_split[3]
                info('检索到用户{}评论过{}，开始写入文件'.format(user_id, house_name))

                file_name = f'{user_id}_{user_name}'  # 文件名称
                content = house_name + ' -> ' + comment  # 写入内容
                save_comment_by_userid(file_name, content)

                if all_user_comment_counter.get(file_name) is None:
                    all_user_comment_counter[file_name] = 1
                else:
                    all_user_comment_counter[file_name] = all_user_comment_counter.get(file_name) + 1

    # 将文件重命名，方便体现用户评论次数

    os.chdir(user_comments_folder)
    user_comments_folder_files = os.listdir()

    txt_name_list = [txt_name for txt_name in user_comments_folder_files if
                     not os.path.isdir(txt_name) and os.path.splitext(txt_name)[1] == '.txt']  # 过滤掉目录

    for user_comments_file in txt_name_list:
        file_name = os.path.splitext(user_comments_file)[0]
        shutil.move(os.path.join(user_comments_folder, user_comments_file)
                    , f'[{all_user_comment_counter.get(file_name)}]{user_comments_file}')

    info('分析用户结束')
