#!/usr/bin/env python
# coding=utf-8


"""
@author: zhangyp
@file: get_str
@time: 2020/5/24 0024 9:02
@desc: 正则表达式，用来匹配提取字符
"""
import re


def get_zhengzedata(str_gs, str_func):
    """
    提取报文的数据方法
    :param str_func:
    :return: 返回匹配到的方法（list）
    """
    zcObject = re.match(str_gs, str_func)
    func_list = []
    if zcObject:
        func_list = zcObject.groups()
    return func_list


def get_data_func_list(str_func):
    """
    提取报文的数据方法
    :param str_func:
    :return: 返回匹配到的方法（list）
    """
    str_gs = "\|{2}.*?\|{2}"
    func_list = re.findall(str_gs, str_func)
    return func_list










