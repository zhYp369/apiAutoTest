#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: data_jiami
@time: 2020/6/5 14:21
@desc: 
"""
import requests

from util.encryption.base64Edit import encode_base64
from util.encryption.hex import sha256hex
from util.data_type_data.edit_json import json_to_dict, dict_to_json
from util.encryption.aes.AES_ECB_pkcs5padding import Aes_ECB
from util.data_type_data.edit_json import inster_new_json
from util.num.get_random import get_random_num
from util.num.get_time import get_time




def get_req_data(api_all):
    """
    对报文进行aes加密
    """
    global_data = api_all.get("global_data").replace("\n", "").replace("\t", "")
    interfaceCode = api_all.get("interfaceCode")
    dataExchangeId = "DZFPQZ"+interfaceCode+ get_time(time_type="%Y%m%d") + get_random_num(9)
    req_data = api_all.get("data")
    appid = api_all.get("other_data").get("appid")
    aeskey = api_all.get("other_data").get("aeskey")
    content = encode_base64(req_data).replace("\n", "").replace("\t", "")
    contentKey_sha256hex = sha256hex(content)
    contentKey_aes = Aes_ECB(aeskey).AES_encrypt(contentKey_sha256hex)
    global_data_dict = json_to_dict(global_data)
    global_data_dict = inster_new_json(global_data_dict, "interface.globalInfo.appId", appid)
    global_data_dict = inster_new_json(global_data_dict, "interface.globalInfo.interfaceCode", interfaceCode)
    global_data_dict = inster_new_json(global_data_dict, "interface.globalInfo.dataExchangeId", dataExchangeId)
    global_data_dict = inster_new_json(global_data_dict, "interface.data.content", content)
    global_data_dict = inster_new_json(global_data_dict, "interface.data.contentKey", contentKey_aes)
    global_data_json = dict_to_json(global_data_dict)
    return global_data_json









