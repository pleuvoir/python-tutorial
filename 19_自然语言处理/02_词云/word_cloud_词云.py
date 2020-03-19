#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pip install wordcloud
"""

import wordcloud

wc = wordcloud.WordCloud(
    background_color='white',  # 设置背景颜色
    font_path='/System/Library/Fonts/Hiragino Sans GB.ttc',  # 设置字体格式
    # mask=mask, # 设置背景图
    max_words=200,  # 最多显示词数
    max_font_size=100,  # 字体最大值
    scale=16  # 调整图片清晰度，值越大越清楚
)

wc.generate('你好啊，中国人')
wc.to_file('world_cloud.png')


