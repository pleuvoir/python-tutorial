#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""文件操作工具类"""
import os


def mkdir_if_necessary(folder: str):
    """
    如果文件夹不存在则创建
    :param folder: 文件夹
    :return:成功则返回True，失败返回False
    """
    try:
        if os.path.exists(folder):
            pass
        else:
            os.mkdir(folder)
    except Exception as e:
        print('创建文件失败', e)
        return False
    return True
