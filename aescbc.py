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

# AES-CBC$B$GJ?J8$r0E9f2=$7$FI|9f$7$F85$KLa$9(B
def main():
    # $BJ?J8(B
    plain = sys.argv[1]
    print "plain  : ", plain.encode('hex')

    # padding$BIU$-J?J8(B
    print "padding: ", padding(plain).encode('hex')

    # $B0E9f80(B
    print "key    : ", aes_key.encode('hex')

    # iv
    iv = "IV for CBC mode."
    print "iv     : ", iv.encode('hex')

    # $B0E9f2=(B
    c = encrypt(plain, aes_key, iv)
    print "encrypt: ", iv.encode('hex') + c.encode('hex')

    # $BI|9f(B
    m = decrypt(c, aes_key, iv)
    print "decrypt: ", m.encode('hex')

    # padding$B%A%'%C%/(B
    print "valid  : ", isvalidpadding(m)

    # $BJ?J8(B
    print "plain  : ", unpadding(m).encode('hex')

if __name__ == "__main__":
    main()

