#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: test_001
@time: 2020/8/24 10:27
@desc: 
"""
import allure
import pytest


apitest_case_data = [
    ("testdata1", "exprcted1", "title1"),
    ("testdata2", "exprcted2", "title2"),
    ("testdata3", "exprcted3", "title3"),
]

dec_list = ["dec1", "dec2", "dec3"]



#     {
#     "test_data": ["testdata1", "testdata2", "testdata3"],
#     "expected": ["expected1", "expected2", "expected3"],
#     "title": ["title1", "title2", "title3"],
#     # "ids": ["dec", "dec", "dec"],
# }


@allure.feature("联合石油接口测试")
@allure.story("订单上传接口")
@allure.title("{title}")
@pytest.mark.parametrize("test_data,expected,title", apitest_case_data)
def test_002(test_data, expected, title):
    print("testdata" + test_data)
    print("expected" + expected)



# def test_001():
#     print("123")