#!/usr/bin/env python
# coding=utf-8

'''
@author: zhangyp
@file: test_postman_api.py
@time: 2019/7/8 20:54
@desc: 测试fpsyy-interface工程接口用例 API
'''

import allure
import pytest
from util.fileEdit.get_data import *
from util.sysEdit.filepathEdit import *
from testcase.test_zwcm.apicommon import *


# 项目名称
project_name = "ZhongWenTianDi"

# 项目测试数据存储地址
project_testData_path = os.path.join(get_project_path(), "testData", project_name)
req_data_dir_path = os.path.join(project_testData_path, "dataFile")


# 获取相关数据文件的数据，项目配置文件数据，接口基本信息数据，测试用例数据
project_config_data = getYamlData(os.path.join(project_testData_path, "project.yml"))[0]
api_config_list = getExcelData(os.path.join(project_testData_path, "fpsyy-interface.xlsx"), 0)
apitest_case_data = getExcelData(os.path.join(project_testData_path, "fpsyy-interface.xlsx"), 1)


# 获取要执行的用例
run_testdata = get_run_testdata(apitest_case_data)


# @allure.feature('中文传媒')
# @allure.story('fpsyy-interface')
@pytest.mark.parametrize('testdata', run_testdata)
def test_timestamp(testdata):
    """
    用例描述：测试不同的timestamp和target
    """
    # 根据api_id获取对应接口基本信息
    api_id = testdata.get("api_id")
    api_config_dict = get_api_config(api_id, api_config_list)

    # get接口url
    host_prot = project_config_data.get("engineering_host").get(api_config_dict.get("api_engineering"))
    api_url = api_config_dict.get("api_url")
    url = host_prot + api_url

    # get接口header
    api_header_str = testdata.get("api_header")
    import json
    api_header_dict = json.loads(s=api_header_str)

    # 请求数据获取
    if testdata.get("is_file") == "yes":
        # 读取存储请求数据的文件，获取请求数据
        req_data_file_path = os.path.join(req_data_dir_path, testdata.get("api_data"))
        with open(req_data_file_path, "r", encoding="utf8") as f:
            req_data_str = f.read()
    else:
        req_data_str = testdata.get("api_data")

    # 请求数据，数据方法处理
    new_req_data_str = updata_req_data(req_data_str)



