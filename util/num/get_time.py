#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: get_time
@time: 2020/8/26 14:46
@desc: 
"""

import time


def get_time(time_type="%Y%m%d%H%M%S"):
    now_time = time.strftime(time_type, time.localtime())
    return now_time