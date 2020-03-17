#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging


class LogLevelFilter(logging.Filter):

    def __init__(self, name='', level=logging.DEBUG):
        super(LogLevelFilter, self).__init__(name)
        self.level = level

    def filter(self, record):
        return record.levelno == self.level


# create logger
format = '%(levelname)s-%(asctime)s-%(threadName)s-%(name)s-%(message)s'
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fh_info = logging.FileHandler('spider.log')
fh_info.setLevel(logging.INFO)
fh_info.setFormatter(format)

fh_debug = logging.FileHandler('spider_debug.log')
fh_debug.setLevel(logging.DEBUG)
fh_debug.setFormatter(format)

fh_error = logging.FileHandler('spider_error.log')
fh_error.setLevel(logging.ERROR)
fh_error.setFormatter(format)

filter_info = LogLevelFilter(level=logging.INFO)
filter_debug = LogLevelFilter(level=logging.DEBUG)
filter_error = LogLevelFilter(level=logging.ERROR)

fh_info.addFilter(filter_info)
fh_debug.addFilter(filter_debug)
fh_error.addFilter(filter_error)

logger.addHandler(fh_info)
logger.addHandler(fh_debug)
logger.addHandler(fh_error)
