#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: jiemi_response
@time: 2020/8/26 17:56
@desc: 
"""
from util.data_type_data.edit_json import json_to_dict, inster_new_json, jiexi_json
from util.encryption.base64Edit import decode_base64


# 将前置接口返的json中的加密部分进行解密，在将整个返回转换dict，返回
def response_jiemi_dict(response):
    response_dict = json_to_dict(response)
    base64_value = jiexi_json(response_dict, "interface.data.content")
    value_dict = json_to_dict(decode_base64(base64_value))
    response_dict = inster_new_json(response_dict, "interface.data.content", value_dict)
    return response_dict
