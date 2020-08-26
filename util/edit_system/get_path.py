#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: get_path
@time: 2020/8/26 16:56
@desc: 
"""
import os


def get_super_dir(now_dir, num):
    for i in range(num):
        now_dir = os.path.dirname(now_dir)
    return now_dir


def get_project_dir():
    now_dir = os.path.dirname(__file__)
    project = get_super_dir(now_dir, 2)
    return project

