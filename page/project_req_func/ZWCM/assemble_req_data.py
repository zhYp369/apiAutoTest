#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: assemble_req_data
@time: 2020/8/26 9:12
@desc: 
"""
from page.api_globle_func.get_all_test_data import get_project_test_data
from page.api_globle_func.get_req_data import *


def get_test_data(all_test_data):
    """
    获取接口信息和数据，更新测试数据，删选执行用例
    """
    # 定义一个字典，用来组装每个用例的测试数据
    api_alltests_list = []
    # 根据参数（用例的所有数据，测试用例，测试报文，接口配置）
    project_config = all_test_data.get("project_config")
    api_config = all_test_data.get("api_config")
    test_cases = all_test_data.get("test_case")
    test_data_file_dir = all_test_data.get("project_testdatafile")
    # 循环每一个用例，进行组装测试数据
    for i in range(len(test_cases)):
        # 定义一个字典，用来组装每个用例的测试数据
        api_alltest_dict = {}
        test_case = test_cases[i]
        api_id = test_case.get("api_id")
        # 获取接口的配置数据
        api_config_data = get_api_config(api_id, api_config)
        # 根据接口配置数据的工程名称，获取对应工程的请求ip和端口，并组装完整接口地址
        url = get_api_hp(api_config_data, project_config) + api_config_data.get("api_url")
        # 组装接口信息字典返回
        api_alltest_dict["case_id"] = test_case.get("case_id")                           # 测试用例id
        api_alltest_dict["api_id"] = test_case.get("api_id")                             # 接口id
        api_alltest_dict["api_engineering"] = api_config_data.get("api_engineering")     # 接口工程名称
        api_alltest_dict["api_name"] = api_config_data.get("api_name")                   # 接口名称
        api_alltest_dict["api_describe"] = api_config_data.get("api_describe")           # 接口描述
        api_alltest_dict["url"] = url                                                    # 测接口地址
        api_alltest_dict["cookie"] = api_config_data.get("cookie")                       # 接口请求cookie
        api_alltest_dict["tonken"] = api_config_data.get("tonken")                       # 接口请求tonken
        api_alltest_dict["method"] = test_case.get("method")                             # 接口请求方式
        api_alltest_dict["header"] = get_api_header(test_case)                           # 接口请求header
        api_alltest_dict["data"] = updata_req_data(get_api_data(test_case, test_data_file_dir))     # 接口请求data
        api_alltest_dict["params"] = updata_req_data(get_api_params(test_case, test_data_file_dir))  # 接口请求params
        api_alltest_dict["expected"] = test_case.get("Expected_results")                 # 接口请求预期结果
        api_alltest_dict["test_discribe"] = test_case.get("test_discribe")               # 用例描述
        api_alltest_dict["other_data"] = project_config.get("other_data")                # 用例其他请求数据
        api_alltest_dict["is_run"] = test_case.get("is_run")                             # 用例是否执行
        if api_alltest_dict["is_run"] == "yes":
            api_alltests_list.append(api_alltest_dict)
        else:
            continue
    return api_alltests_list


def assemble_testdata_expected_title(all_runtest_encryption_data):
    case_datas = []
    for i in range(len(all_runtest_encryption_data)):
        run_testdata = all_runtest_encryption_data[i]
        expected = run_testdata.get("expected")
        title = run_testdata.get("case_id") + "@" + run_testdata.get("test_discribe")
        args_tuple = (run_testdata, expected, title)
        case_datas.append(args_tuple)
    return case_datas


def get_testData_expected_title():
    all_test_data = get_project_test_data()
    # 获取所有用例测试数据
    api_alltests_list = get_test_data(all_test_data)
    # 组装testcase, title, expected
    testdata_expected_title = assemble_testdata_expected_title(api_alltests_list)
    return testdata_expected_title