#!/usr/bin/env python
# coding=utf-8


"""
@author: zhangyp
@file: apicommon
@time: 2020/5/17 0017 17:05
@desc: 
"""

from util.sysEdit.filepathEdit import *
from util.zhengzebiaodashi.getdata_fromzhengze import get_data_func_list
from util.GlobeTestDataFunction.dataFunction import getfunc_value


def get_run_testdata(testdatas):
    """

    :param testdata: 传入全部测试用例
    :return: 返回需要运行的测试用例
    """
    run_testdatas = []
    for i in range(len(testdatas)):
        if testdatas[i].get("is_run") == "yes":
            run_testdatas.append(testdatas[i])
    return run_testdatas


def get_api_config(api_id, api_config_list):
    """
    根据传入的接口id，返回接口信息api_config_dict
    :param api_id:
    :param api_config_list:
    :return: 返回接口信息api_config_dict
    """
    api_config_dict = {}
    for i in range(len(api_config_list)):
        if api_config_list[i].get("api_id") == api_id:
            api_config_dict = api_config_list[i]
            break
        else:
            continue
    return api_config_dict


def updata_req_data(req_data):
    """
    将请求报文里的数据进行
    :param req_data:
    :return:
    """
    # 获取请求数据包含的方法，返回list
    req_data_func_list = get_data_func_list(req_data)

    # 根据方法列表，返回方法和方法对应的值
    req_data_FuncAndValue_dict = {}
    for i in range(len(req_data_func_list)):
        req_data_FuncAndValue_dict[req_data_func_list[i]] = getfunc_value(req_data_func_list[i])

    # 将请求数据的方法换成对应的值

    for k, v in req_data_FuncAndValue_dict.items():
        req_data = str(req_data).replace(k, v)
    return req_data
