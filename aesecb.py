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

# AES-ECBで平文を暗号化して復号して元に戻す
def main():
    # 平文
    plain = sys.argv[1]
    print "plain  : ", plain.encode('hex')

    # 暗号鍵
    print "key    : ", aes_key.encode('hex')

    # 暗号化
    c = encrypt(plain, aes_key)
    print "encrypt: ", c.encode('hex')

    # 復号
    m = decrypt(c, aes_key)
    print "decrypt: ", m.encode('hex')

    # 平文
    print "plain  : ", m.encode('hex')

if __name__ == "__main__":
    main()

