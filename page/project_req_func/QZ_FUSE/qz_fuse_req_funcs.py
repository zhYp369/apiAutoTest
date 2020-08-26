#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: zwcm_req_funcs
@time: 2020/6/5 13:07
@desc:
"""

from page.api_globle_func.api_req import req_http
from page.project_req_func.QZ_FUSE.edit_dependent import save_dependent, api_all_add_dependent
from page.project_req_func.QZ_FUSE.fpt_rhqz_jiami import get_req_data


def rhqz_req(api_all):
    """
    融合前置接口请求公共方法
    :param api_all:
    :return:
    """
    url = api_all.get("url")
    method = api_all.get("method")
    kwargs = {}
    kwargs["headers"] = api_all.get("header")
    if api_all.get("dependent") == "yes":
        api_all = api_all_add_dependent(api_all)
    kwargs["data"] = get_req_data(api_all)
    kwargs["verify"] = False
    respon = req_http(url=url, method=method, kwargs=kwargs)
    respon.encoding = "utf-8"
    respon_text = respon.text.replace("\n", "").replace("\t", "")
    if api_all.get("Be_dependent") == "yes":
        save_dependent(api_all, respon_text)
    return respon_text



