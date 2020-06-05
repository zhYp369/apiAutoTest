#!/usr/bin/env python
# coding=utf-8

'''
@author: zhangyp
@file: test_postman_api.py
@time: 2019/7/8 20:54
@desc: 测试fpsyy-interface工程接口用例 API
'''

# import allure
# import pytest
# from util.sysEdit.filepathEdit import *
from util.fileEdit.get_data import *
from testcase.test_zwcm.apicommon import *
from page.api_globle_func.edit_api_data import get_api_all, updata_req_data_for_api_all
from page.project_req_func.ZWCM.zwcm_req_funcs import globle_req


# 本工程地址

project_testData_path = os.path.join(get_project_path(), "testData", "ZhongWenTianDi")
req_data_dir_path = os.path.join(project_testData_path, "dataFile")


# 获取相关数据文件的数据，项目配置文件数据，接口基本信息数据，测试用例数据
project_config_data = getYamlData(os.path.join(project_testData_path, "project.yml"))[0]
api_config_list = getExcelData(os.path.join(project_testData_path, "fpsyy-interface.xlsx"), 0)
apitest_case_data = getExcelData(os.path.join(project_testData_path, "fpsyy-interface.xlsx"), 1)


run_testdata = get_run_testdata(apitest_case_data)


testdata = run_testdata[0]

# 获取接口信息和测试数据
api_all_dict = get_api_all(testdata, api_config_list, project_config_data, req_data_dir_path)

# 更新接口测试数据
api_all_dict = updata_req_data_for_api_all(api_all_dict)

# 根据接口信息选择对应的接口请求方法
respon = globle_req(api_all_dict)

print(respon)

# if api_all_dict.get()













