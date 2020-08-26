#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: test
@time: 2020/8/26 13:50
@desc: 
"""

from Crypto.Cipher import AES
import base64
import json
import requests


class Aes_ECB(object):
    def __init__(self,key):
        self.key = key
        self.MODE = AES.MODE_ECB
        self.BS = AES.block_size
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)
        self.unpad = lambda s: s[0:-ord(s[-1])]

    # str不是16的倍数那就补足为16的倍数
    def add_to_16(value):
        while len(value) % 16 != 0:
            value += '\0'
        return str.encode(value)  # 返回bytes


    def AES_encrypt(self, text):
        aes = AES.new(Aes_ECB.add_to_16(self.key), self.MODE)  # 初始化加密器
        encrypted_text = str(base64.encodebytes(aes.encrypt(Aes_ECB.add_to_16(self.pad(text)))), encoding='utf-8').replace('\n', '')     #这个replace大家可以先不用，然后在调试出来的结果中看是否有'\n'换行符
        # 执行加密并转码返回bytes
        return encrypted_text

    # 解密
    def AES_decrypt(self, text):
        # 初始化加密器
        aes = AES.new(Aes_ECB.add_to_16(self.key), self.MODE)
        # 优先逆向解密base64成bytes
        base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
        decrypted_text = self.unpad(aes.decrypt(base64_decrypted).decode('utf-8'))
        decrypted_code = decrypted_text.rstrip('\0')
        return decrypted_code



