#!/usr/bin/env python
# coding=utf-8

'''
@author: lingshu
@file: test_postman_api.py
@time: 2019/7/8 20:54
@desc: 测试postman API
'''

import allure
import pytest
from util.fileEdit.get_data import *
from util.sysEdit.filepathEdit import *
from testcase.test_zwcm.apicommon import *


# 本工程地址
project_path = get_project_path()


# 获取
project_config_data = getYamlData(os.path.join(project_path, "testData", "ZhongWenTianDi", "project.yml"))
engineering_config_data = getExcelData(os.path.join(project_path, "testData", "ZhongWenTianDi", "fpsyy- .xlsx"), 0)
api_config_data = getExcelData(os.path.join(project_path, "testData", "ZhongWenTianDi", "fpsyy-interface.xlsx"), 1)
apitest_case_data = getExcelData(os.path.join(project_path, "testData", "ZhongWenTianDi", "fpsyy-interface.xlsx"), 2)
run_testdata = get_run_testdata(apitest_case_data)


@allure.feature('中文传媒')
@allure.story('fpsyy-interface')
@pytest.mark.parametrize('testdata',run_testdata)
def test_timestamp(testdata):
    """
    用例描述：测试不同的timestamp和target
    """
    # 解析接口请求url
    url = get_api_url(engineering_config_data, api_config_data, testdata)
    # 传入url和接口数据，进行请求接口，返回接口相应结果
    r = api_req(url, testdata)
    # 对相应结果进行断言
    assert_api(r, testdata)
