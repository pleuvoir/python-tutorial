#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

pip3 install pillow
"""

from PIL import Image

if __name__ == '__main__':
    img = Image.open('CTP简化交易工作流程.png') #返回一个Image对象
    print('宽：%d,高：%d'%(img.size[0],img.size[1]))
    basewidth = 780
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))

    print(basewidth,hsize)
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)

    img.save('CTP简化交易工作流程_.png')
