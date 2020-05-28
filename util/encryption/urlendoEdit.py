#!/usr/bin/env python
# coding=utf-8


"""
@author: zhyp
@file: urlendoEdit
@time: 2020/5/16 0016 17:52
@desc: 处理url字符转换
"""

from urllib.parse import quote_plus


def url_encode(url):
    """
    对url进行参数urlencode
    :param url:
    :return:
    """
    value = quote_plus(url, encoding="utf-8")
    return value