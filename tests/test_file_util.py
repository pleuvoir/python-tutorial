#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import unittest

from tests.file_util import mkdir_if_necessary

"""单元测试"""


class TestFileUtil(unittest.TestCase):

    def test_mkdir_if_necessary(self):
        self.assertFalse(mkdir_if_necessary('folder'))
        self.assertTrue(mkdir_if_necessary(os.path.join(os.getcwd(), 'folder')))


if __name__ == '__main__':
    unittest.main()
