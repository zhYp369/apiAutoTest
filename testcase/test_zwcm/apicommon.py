#!/usr/bin/env python
# coding=utf-8


"""
@author: 
@file: apicommon
@time: 2020/5/17 0017 17:05
@desc: 
"""


def get_run_testdata(testdatas):
    """

    :param testdata: 传入全部测试用例
    :return: 返回需要运行的测试用例
    """
    run_testdatas = []
    for testdata in range(len(testdatas)):
        if dict(testdata).get("is_run") == "yes":
            run_testdatas.append(testdata)
    return run_testdatas


def get_api_url(engineering_config_data, api_config_data, testdata):
    """
    根据 工程配置数据、接口文档配置数据、测试用例数据获取对应接口的url
    :param engineering_config_data: 工程配置数据
    :param api_config_data: 接口文档配置数据
    :param testdata: 测试用例数据
    :return: 返回接口的请求url
    """

    # 从engineeringConfig获取接口的ip和端口
    host = engineering_config_data[0].get("host")
    port = engineering_config_data[0].get("port")

    # 根据测试用例的接口id从apiFile获取接口地址
    api_id = testdata.get("api_id")
    api_url = ""
    for i in range(len(api_config_data)):
        if api_config_data.get("api_id") == api_id:
            api_url = api_config_data.get("api_url")
            break
        else:
            continue
    url = host + ":" + port + api_url
    return url


def api_req(url, testdata):
    """
    传入接口地址和接口数据，处理请求数据，进行请求，获得返回结果
    :param url:
    :param testdata:
    :return:
    """

    pass


def assert_api(r, testdata):
    """

    :param r:
    :param testdata:
    :return:
    """
    pass
