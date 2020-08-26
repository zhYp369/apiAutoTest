#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: api_req
@time: 2020/6/5 13:25
@desc: 
"""

import requests


def req_http(method, url, kwargs):
    """

    :param method:
    :param url:
    :param kwargs: {headers=headers, data=payload, files= "", json="", params="", timeout=3000, verify=False}
    :return:
    """
    respon = requests.request(url=url, method=method, **kwargs)
    return respon



