#!/usr/bin/env python
# coding=utf-8


"""
@author: zhangyp
@file: aesEdit
@time: 2020/5/16 0016 17:39
@desc: 封装aes加密方法
"""


from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


def pad_key(key):
    """
    秘钥字符不够16不够16，大于16补够16倍数
    :param key:
    :return:
    """
    while len(key) % 16 != 0:
        key += b' '
    return key


def pad(text):
    """
    加密字符不够16不够16，大于16补够16倍数
    :param text:
    :return:
    """
    while len(text) % 16 != 0:
        text += b' '
    return text


def en_ase_str(key, text):
    """
    对字符aes进行加密
    :param key:
    :param text:
    :return:
    """
    key = key.encode(encoding="utf-8")
    text = text.encode(encoding="utf-8")
    # text = pad(text)
    # key = pad_key(key)
    # 进行加密算法，模式ECB模式，把叠加完16位的秘钥传进来
    aes = AES.new(key, AES.MODE_ECB)
    encrypted_text = aes.encrypt(text)
    encrypted_text = b2a_hex(encrypted_text).decode(encoding="utf-8")
    return encrypted_text


def de_ase_str(key, text):
    """
    对字符进行aes加密
    :param key:
    :param text:
    :return:
    """
    key = key.encode(encoding="utf-8")
    text = text.encode(encoding="utf-8")
    text = a2b_hex(text)
    key = pad_key(key)
    aes = AES.new(key, AES.MODE_ECB)
    decrypted_text = aes.decrypt(text)
    decrypted_text = decrypted_text.rstrip(b" ")
    return decrypted_text.decode(encoding="utf-8")
