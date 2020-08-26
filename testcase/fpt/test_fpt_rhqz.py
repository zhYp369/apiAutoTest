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

from page.project_req_func.QZ_FUSE.qz_fuse_assemble import get_testData_expected_title
from page.project_req_func.QZ_FUSE.qz_fuse_req_funcs import rhqz_req
from page.project_req_func.QZ_FUSE.qz_fuse_assert import assert_result_in


# 获取相关数据文件的数据，项目配置文件数据，接口基本信息数据，测试用例数据
test_data_dict = get_testData_expected_title()


@allure.feature("中文天地项目接口测试")
@allure.story("订单上传接口")
@allure.title("{title}")
@pytest.mark.parametrize('testdata, expected, title', test_data_dict)
@pytest.mark.A
def test_timestamp(testdata, expected, title):
    """
    用例描述：测试不同的timestamp和target
    """
    # 根据接口信息选择对应的接口请求方法
    respon = rhqz_req(testdata)
    # allure.attach(respon)

    # 校验返回结果
    assert_result_in(respon, expected)






