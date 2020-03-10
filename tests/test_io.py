#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

if __name__ == '__main__':
    dirname = os.getcwd()
    print(dirname) #/Users/pleuvoir/dev/space/git/python-tutorial/tests

    path_dirname = os.path.dirname(dirname)
    print(path_dirname)  ##/Users/pleuvoir/dev/space/git/python-tutorial

    _source_root = os.path.dirname(path_dirname)
    print(_source_root) #/Users/pleuvoir/dev/space/git

    print(os.path.abspath(_source_root)) #/Users/pleuvoir/dev/space/git
