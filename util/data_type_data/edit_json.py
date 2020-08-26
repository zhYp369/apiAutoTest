#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: edit_json
@time: 2020/8/26 11:31
@desc: 
"""


import json


# 字典转换json
def dict_to_json(dict_data):
    json_data = json.dumps(dict_data)
    return json_data


# 对象转json数据
def obj_to_json(cls_ob):
    dict_data = cls_ob.__dict__  # 将对象转成dict字典
    json_data = json.dumps(obj=dict_data)     # 将对象转成dict字典
    return json_data


# json数据转成dict字典
def json_to_dict(json_data):
    dict_data = json.loads(s=json_data)
    return dict_data


# json数据转成对象
def json_to_obj(json_data, cls):
    dict_data = json.loads(s=json_data)
    cls_ob = cls
    cls_ob.__dict__ = dict_data
    return cls_ob


# dict转换json的文件
def dict_to_json_write_file(json_file, dict_data):
    with open(json_file, 'w') as f:
        json.dump(dict_data, f)


# json的文件转换dict
def json_file_to_dict(json_file):
    with open(json_file, 'r') as f:
        dict_data = json.load(fp=f)
    return dict_data


# 校验json里面是否有对应的key
def key_excit_json(json_1, key):
    json_1 = json.dumps(json_1)
    keylsit = key.split(".")
    if keylsit[-1] in json_1:
        return True
    else:
        return False


# 解析返回的json获得关键key值
def jiexi_json(json_data, key):
    a = key.split(".")
    value = json_data
    for i in a:
        value = value.get(i, "null")
        if value == "null":
            break
    return value


# 修改json中某个key的值
def inster_new_json(json_data, key, value):
    key_ = key.split(".")
    key_length = len(key_)
    i = 0
    json_data = dict(json_data)
    a = json_data
    while i < key_length:
        if i + 1 == key_length:
            a[key_[i]] = value
            i = i + 1
        else:
            a = a[key_[i]]
            i = i + 1
    return json_data
