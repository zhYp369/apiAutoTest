#!/usr/bin/env python
# coding=utf-8


"""
@author: zhyp
@file: md5Edit
@time: 2020/5/16 0016 17:16
@desc: 
"""

import hashlib


def md5_str(test):
    """
    md5加密
    :param test:
    :return:
    """
    hl = hashlib.md5()
    hl.update(test.encode(encoding='utf-8'))
    test_md5 = hl.hexdigest()
    return test_md5
