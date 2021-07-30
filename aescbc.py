#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from Crypto.Cipher import AES

block_size = 16
aes_key = "\n" * block_size

def padding(s):
    i = block_size - len(s) % block_size
    pad = chr(i) * i
    return s + pad

def unpadding(s):
    return s[0:-ord(s[-1])]

def isvalidpadding(s):
    i = ord(s[-1])
    return 0 < i and i <= block_size and s[-1]*i == s[-i:]

def encrypt(p, key, iv):
    return AES.new(key, AES.MODE_CBC, iv).encrypt(padding(p))

def decrypt(c, key, iv):
    return AES.new(key, AES.MODE_CBC, iv).decrypt(c)

def check_padding(c, iv):
    return isvalidpadding(decrypt(c, aes_key, iv))

# AES-CBCで平文を暗号化して復号して元に戻す
def main():
    # 平文
    plain = sys.argv[1]
    print "plain  : ", plain.encode('hex')

    # padding付き平文
    print "padding: ", padding(plain).encode('hex')

    # 暗号鍵
    print "key    : ", aes_key.encode('hex')

    # iv
    iv = "IV for CBC mode."
    print "iv     : ", iv.encode('hex')

    # 暗号化
    c = encrypt(plain, aes_key, iv)
    print "encrypt: ", iv.encode('hex') + c.encode('hex')

    # 復号
    m = decrypt(c, aes_key, iv)
    print "decrypt: ", m.encode('hex')

    # paddingチェック
    print "valid  : ", isvalidpadding(m)

    # 平文
    print "plain  : ", unpadding(m).encode('hex')

if __name__ == "__main__":
    main()

