#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil

shutil.rmtree('要清空的文件夹，无视里面是否有内容')
shutil.move('原文件夹/原文件名', '目标文件夹/目标文件名')