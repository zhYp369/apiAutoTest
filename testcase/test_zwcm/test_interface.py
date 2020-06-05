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
from page.api_globle_func.edit_api_data import get_api_all, updata_req_data_for_api_all
from page.project_req_func.ZWCM.zwcm_req_funcs import globle_req

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


@allure.feature('中文传媒')
@allure.story('fpsyy-interface')
@pytest.mark.parametrize('testdata', run_testdata)
def test_timestamp(testdata):
    """
    用例描述：测试不同的timestamp和target
    """
    # 获取接口信息和测试数据
    api_all_dict = get_api_all(testdata, api_config_list, project_config_data, req_data_dir_path)

    # 更新接口测试数据
    api_all_dict = updata_req_data_for_api_all(api_all_dict)

    # 根据接口信息选择对应的接口请求方法
    respon = globle_req(api_all_dict)
    allure.attach(respon)
    print(respon)



