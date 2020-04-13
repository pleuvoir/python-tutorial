#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser

config = configparser.ConfigParser()

config.read('simple.ini')

#不会包含DEFAULT 所以我们写的时候不建议用DEFAULT，不然遍历时还要单独处理，DEFAULT会包含在所有的section里
print(config.sections(),type(config.sections())) # ['bitbucket.org', 'topsecret.server.com'] <class 'list'>

# 输出所有

for section in config.sections():
    print(f'开始输出{section}')
    for key, value in config[section].items():
        print(key, value)
    print(f'结束输出{section}\n')

print('*' * 36)

default_group = config['DEFAULT']
bitbucket_org_group = config['bitbucket.org']
topsecret_server_com_group = config['topsecret.server.com']

for key, value in default_group.items():
    print(key, value)

print(default_group.get('ServerAliveInterval', '?'))
print(default_group.get('ServerAliveInterval1', '默认'))
print(default_group.getint('ServerAliveInterval'))
