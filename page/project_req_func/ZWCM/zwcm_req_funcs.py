#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: zwcm_req_funcs
@time: 2020/6/5 13:07
@desc:
"""
from page.project_req_func.ZWCM.data_jiami import get_aes_message, get_sign_message
from page.api_globle_func.api_req import req_http


def globle_req(api_all):
    """
    中文传媒接口请求公共方法
    :param api_all:
    :return:
    """
    url = api_all.get("url")
    method = api_all.get("method")
    kwargs = {}
    kwargs["headers"] = api_all.get("header")
    print(api_all.get("other_data").get("aesKey"))
    print(api_all.get("data"))
    kwargs["data"] = get_aes_message(api_all.get("other_data").get("aesKey"), api_all.get("data"))
    kwargs["params"] = api_all.get("params")
    kwargs["verify"] = False
    respon = req_http(url=url, method=method, **kwargs)
    return respon



