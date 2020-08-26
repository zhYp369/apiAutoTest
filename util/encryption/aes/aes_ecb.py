#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: aes_ecb
@time: 2020/8/26 12:32
@desc: 
"""


"""
ECB没有偏移量
"""
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')


# 加密函数
def encrypt(aeskey, text):
    key = aeskey.encode('utf-8')
    mode = AES.MODE_ECB
    text = add_to_16(text)
    cryptos = AES.new(key, mode)
    cipher_text = cryptos.encrypt(text)
    return b2a_hex(cipher_text)


# 解密后，去掉补足的空格用strip() 去掉
def decrypt(text):
    key = '9999999999999999'.encode('utf-8')
    mode = AES.MODE_ECB
    cryptor = AES.new(key, mode)
    plain_text = cryptor.decrypt(a2b_hex(text))
    return bytes.decode(plain_text).rstrip('\0')


if __name__ == '__main__':
    KEY = "HAOHUAN_PASSWORD"
    decrypt_data = '{"success":1,"type":"2","uniqueId":"9097_9097_100110_1581489198_5288"}'
    a = encrypt(KEY, decrypt_data)
    print(a)