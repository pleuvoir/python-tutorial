#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba
from jieba import analyse

"""
pip install jieba
如果词语分的不正确，那么可以自己配置txt文件，具体再查
"""

text = '我来到北京天安门，看见毛主席在向我挥手，乾清宫的大门向我敞开，我真的很高兴。'

jieba_cut = jieba.cut(text)
print('/'.join(jieba_cut))

tags = analyse.extract_tags(text, topK=5)
print(type(tags), tags) #<class 'list'> ['天安门', '敞开', '挥手', '毛主席', '清宫']
