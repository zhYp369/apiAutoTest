#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: data_jiami
@time: 2020/6/5 14:21
@desc: 
"""

import hashlib
from Crypto.Cipher import AES
import hmac
from binascii import b2a_hex, a2b_hex


a = [53, 54, 50, 97, 59, 53, 110, 121, 45, 99, 57, 51, 49, 45, 52, 98, 50, 56, 45, 97, 53, 101, 50, 55, 46, 19, 51, 52, 97, 50, 74, 16, 49, 56, 98, 54]
sg_key = bytearray(a)
ae_key = "ABCD123dJKHger34"


def get_aes_message(key, value):
    """
    对报文进行aes加密
    """
    # key -> sha1prng_key
    signature = hashlib.sha1(key.encode()).digest()
    signature = hashlib.sha1(signature).digest()
    aes_key = bytes.fromhex(''.join(['%02x' % i for i in signature])[:32])
    crypto = AES.new(aes_key, AES.MODE_ECB)
    # padding content with pkcs5
    block_size = AES.block_size
    append_size = block_size - len(value.encode('utf-8')) % block_size
    padding_value = value + append_size * chr(append_size)
    return ''.join(['%02x' % i for i in crypto.encrypt(str.encode(padding_value))])


def get_sign_message(message):
    """
    对报文签名
    """
    signature = hmac.new(sg_key, bytes(message, encoding='utf-8'), digestmod=hashlib.sha256).digest()
    str_sig = b2a_hex(signature).decode(encoding="utf-8")
    return str_sig