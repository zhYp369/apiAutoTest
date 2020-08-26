#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: edit_data
@time: 2020/8/25 11:32
@desc: 
"""
import json
import os
from util.zhengzebiaodashi.getdata_fromzhengze import get_data_func_list
from util.GlobeTestDataFunction.dataFunction import getfunc_value


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


def get_api_config(api_id, api_config_list):
    """
    根据传入的接口id，和接口文档数据，获取对应接口的配置数据
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


def get_api_hp(api_config_data, project_config):
    engineering = api_config_data.get("api_engineering")
    host_prot = project_config.get("engineering_hp").get(engineering)
    return host_prot


def get_api_header(test_case):
    header = json.loads(s=test_case.get("api_header"))
    return header


# 获取请求数据data
def get_api_data(test_case, test_data_file_dir):
    if test_case.get("data_IsFlie") == "yes":
        # 读取存储请求数据的文件，获取请求数据
        req_data_file_path = os.path.join(test_data_file_dir, test_case.get("api_data"))
        with open(req_data_file_path, "r", encoding="utf8") as f:
            req_data_str = f.read()
    elif test_case.get("data_IsFlie") == "no":
        req_data_str = test_case.get("api_data")
    else:
        req_data_str = ""
    return req_data_str


# 获取请求数据params
def get_api_params(testcase, test_data_file_dir):
    if testcase.get("params_IsFlie") == "yes":
        # 读取存储请求数据的文件，获取请求数据
        req_data_file_path = os.path.join(test_data_file_dir, testcase.get("api_params"))
        with open(req_data_file_path, "r", encoding="utf8") as f:
            req_params_str = f.read()
    elif testcase.get("params_IsFlie") == "no":
        req_params_str = testcase.get("api_params")
    else:
        req_params_str = ""
    return req_params_str


# 获取请求数据params
def get_api_global(api_config_data, test_data_file_dir):
    # 读取存储请求数据的文件，获取请求数据
    req_data_file_path = os.path.join(test_data_file_dir, api_config_data.get("global_path"))
    with open(req_data_file_path, "r", encoding="utf8") as f:
        req_params_str = f.read()
    return req_params_str



