#!/usr/bin/env python
# coding=utf-8

'''
@author: zhangyp
@file: test_postman_api.py
@time: 2019/7/8 20:54
@desc: 测试fpsyy-interface工程接口用例 API
'''

import os
import json
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


def get_api_all(testdata, api_config_list, project_config_data, req_data_dir_path):
    """
    获取接口信息和数据，用字典的形式返回
    :param testdata:
    :param api_config_list:
    :param project_config_data:
    :param req_data_dir_path:
    :return:
    """
    api_all_dict = {}

    # 根据api_id获取对应接口基本信息
    api_id = testdata.get("api_id")
    api_config_dict = get_api_config(api_id, api_config_list)

    # get接口url
    host_prot = project_config_data.get("engineering_host").get(api_config_dict.get("api_engineering"))
    api_url = api_config_dict.get("api_url")
    url = host_prot + api_url

    # get接口header
    api_header_str = testdata.get("api_header")
    api_header_dict = json.loads(s=api_header_str)

    # 请求数据data获取
    if testdata.get("data_IsFlie") == "yes":
        # 读取存储请求数据的文件，获取请求数据
        req_data_file_path = os.path.join(req_data_dir_path, testdata.get("api_data"))
        with open(req_data_file_path, "r", encoding="utf8") as f:
            req_data_str = f.read()
    elif testdata.get("data_IsFlie") == "no":
        req_data_str = testdata.get("api_data")
    else:
        req_data_str = ""

    # 请求数据params获取
    if testdata.get("params_IsFlie") == "yes":
        # 读取存储请求数据的文件，获取请求数据
        req_data_file_path = os.path.join(req_data_dir_path, testdata.get("api_params"))
        with open(req_data_file_path, "r", encoding="utf8") as f:
            req_params_str = f.read()
    elif testdata.get("params_IsFlie") == "no":
        req_params_str = testdata.get("api_params")
    else:
        req_params_str = ""

    # # 请求数据，数据方法处理
    # new_req_data_str = updata_req_data(req_data_str)
    # new_req_params_str = updata_req_data(req_params_str)
    # 组装接口信息字典返回
    api_all_dict["url"] = url
    api_all_dict["header"] = api_header_dict
    api_all_dict["data"] = req_data_str
    api_all_dict["params"] = req_params_str
    api_all_dict["method"] = api_config_dict.get("method")
    api_all_dict["cookie"] = api_config_dict.get("cookie")
    api_all_dict["tonken"] = api_config_dict.get("tonken")
    api_all_dict["apiid"] = api_config_dict.get("api_id")
    api_all_dict["apiproject"] = api_config_dict.get("api_project")
    api_all_dict["apiengineering"] = api_config_dict.get("api_engineering")
    api_all_dict["project_DB"] = project_config_data.get("project_DB")
    api_all_dict["other_data"] = project_config_data.get("other_data")
    return api_all_dict


def updata_req_data_for_api_all(api_all):
    api_all["data"] = updata_req_data(api_all.get("data"))
    api_all["params"] = updata_req_data(api_all.get("params"))
    return api_all


def req_api(api_all):
    """
    根据接口信息选择对应的接口请求方法
    :param api_all:
    :return:
    """
    apiproject = api_all.get("apiproject")
    apiengineering = api_all.get("apiengineering")
    apiid = api_all.get("apiid")
    print(apiproject)
    print(apiengineering)
    print(apiid)
    pass

