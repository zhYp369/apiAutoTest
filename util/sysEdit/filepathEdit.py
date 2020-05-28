#!/usr/bin/env python
# coding=utf-8


"""
@author: lingshu
@file: test_postman_api.py
@time: 2019/7/8 20:54
@desc: 测试postman API
"""


import os


def get_project_path():
    project_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    return project_path

