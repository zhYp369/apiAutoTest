#!/usr/bin/env python
# coding=utf-8


"""
@author: 
@file: dataFunction
@time: 2020/5/24 0024 8:56
@desc: 
"""

from util.zhengzebiaodashi.getdata_fromzhengze import get_data_func_list, get_zhengzedata
from util.num.get_random import *


def check_function_entrance(req_data_str):
    """
    判断请求报文是否有数据方法
    :param req_data_str:
    :return: list如果为空则返回false，如果不为空，则返回list
    """
    req_func_list = get_data_func_list(req_data_str)
    if len(req_func_list) > 0:
        return req_func_list
    else:
        return False


def getfunc_value(func_str):
    value = ""
    zz_gs = ".*\((.*?)\).*"
    if "readen_str" in func_str:
        n = get_zhengzedata(zz_gs, func_str)[0]
        print(n)
        value = get_random_str(int(n))
        return value

    if "readen_int" in func_str:
        n = get_zhengzedata(zz_gs, func_str)[0]
        print(n)
        value = get_random_num(int(n))
        return value

    if "time_str" in func_str:
        type_time = get_zhengzedata(zz_gs, func_str)[0]
        print(type_time)
        value = get_time_str(type_time)
        return value














