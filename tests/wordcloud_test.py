#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wordcloud
from jieba import analyse

wc = wordcloud.WordCloud(
    background_color='white',  # 设置背景颜色
    font_path='/System/Library/Fonts/Hiragino Sans GB.ttc',  # 设置字体格式
    # mask=mask, # 设置背景图
    max_words=200,  # 最多显示词数
    max_font_size=100,  # 字体最大值
    scale=16  # 调整图片清晰度，值越大越清楚
)

text = '如果可以，我愿意活在自己挖好的井里，醒的时候抬头看天，困得时候低头睡觉。'

tags = analyse.extract_tags(text, topK=3)

wc.generate(' '.join(tags))
wc.to_file('world_cloud.png')

# wc.generate(' '.join(tags))
# wc.to_file('world_cloud2.png')
