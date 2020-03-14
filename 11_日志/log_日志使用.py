#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

log = logging.getLogger(name=__name__)
"""
https://docs.python.org/3/library/logging.html#logrecord-attributes
"""

print(logging.BASIC_FORMAT)  # %(levelname)s:%(name)s:%(message)s

format = '%(levelname)s-%(asctime)s-%(threadName)s-%(name)s-%(message)s'

# 默认级别是warning
logging.basicConfig(level='INFO', filename='python-tuturial.log', filemode='w', format=format)

log.debug('你好啊')
log.info('你好啊')
log.warning('你好啊')
log.error('你好啊')
log.critical('你好啊')


log.info('你好啊{}'.format('pleuvoir'))