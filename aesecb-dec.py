#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from Crypto.Cipher import AES

block_size = 16
aes_key = "\n" * block_size

def encrypt(p, key):
    return AES.new(key, AES.MODE_ECB).encrypt(p)

def decrypt(c, key):
    return AES.new(key, AES.MODE_ECB).decrypt(c)

# AES-ECBで平文を復号して元に戻す
def main():
    # 暗号文
    encrypt = sys.argv[1]
    print "encrypt: ", encrypt

    # 暗号鍵
    print "key    : ", aes_key.encode('hex')

    # 復号
    m = decrypt(encrypt.decode('hex'), aes_key)
    print "decrypt: ", m.encode('hex')

if __name__ == "__main__":
    main()

