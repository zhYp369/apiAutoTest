#!/usr/bin/env python
# coding=utf-8


"""
@author: 
@file: get_random
@time: 2020/5/24 0024 10:29
@desc: 
"""


import random
import time


def random_str(digits=True, lowercase=True, uppercase=True, symbol=True, slen=10):
    seed = ''
    seed = seed + '1234567890' if digits else seed+''
    seed = seed + 'abcdefghijklmnopqrstuvwxyz' if lowercase else seed + ''
    seed = seed + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if uppercase else seed + ''
    seed = seed + '!@#$%^&*()_+=-' if symbol else seed + ''
    if len(seed)==0:
        return None
    sa = []
    for i in range(slen):
      sa.append(random.choice(seed))
    return ''.join(sa)


def generate_random_Ssn(randomlength=16):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


def get_random_STR(randomlength=16):
    """
    生成一个指定长度的大写字母随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


def get_random_str(randomlength=16):
    """
    生成一个指定长度的小写写字母随机字符串
    """
    random_str = ''
    base_str = 'abcdefghigklmnopqrstuvwxyz'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


def get_random_num(randomlength=16):
    """
    生成一个指定长度的数字随机字符串
    """
    random_str = ''
    base_str = '0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


def get_time_str(time_tyle="%Y%m%d%H%M%S"):
    """
    根据传入的时间格式，返回一个时间的字符串
    """
    now = time.localtime(time.time())
    time_str = time.strftime(time_tyle, now)
    return time_str
