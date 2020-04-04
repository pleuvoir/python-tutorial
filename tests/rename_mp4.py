#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

folder = '/Users/pleuvoir/store/04 baiduyun/Go语言从入门到实战/'

os.chdir(os.path.abspath(folder))

mp4_name_list = [mp4_name for mp4_name in os.listdir() if os.path.splitext(mp4_name)[1] == '.mp4']

print(len(mp4_name_list))

for mp4_file in mp4_name_list:
    file_name = os.path.splitext(mp4_file)[0]
    file_suffix = os.path.splitext(mp4_file)[1]
    clear_mp4_name = file_name.replace('【javazx.com[Java自学网]】', '').replace('[www.javazx.com]', '').replace('_', '')

    print('原名字 {}，新名字 {}'.format(file_name, clear_mp4_name))
    shutil.move(os.path.join(folder, mp4_file)
                , f'{clear_mp4_name}{file_suffix}')
