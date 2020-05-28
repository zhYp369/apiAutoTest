#!/usr/bin/env python
# coding=utf-8


"""
@author: zhyp
@file: md5Edit
@time: 2020/5/16 0016 17:16
@desc:
"""

import base64


def encode_base64(test):
    """
    base64加密
    :param test:
    :return:
    """
    base64_bytes = base64.encodebytes(test.encode(encoding="utf-8"))
    base64_str = base64_bytes.decode(encoding="utf-8")
    return base64_str


def decode_base64(test):
    """
    base64解密
    :param test:
    :return:
    """
    base64_bytes = test.encode(encoding="utf-8")
    test_bytes = base64.decodebytes(base64_bytes)
    test_str = test_bytes.decode(encoding="utf-8")
    return test_str
