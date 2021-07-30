#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from Crypto.Cipher import AES
import aescbc

# 暗号文を復号しパディングが正しければTrueを返す
# 攻撃する側はkeyを知らない
# そこで攻撃される側に復号させて正しく復号できたかどうかの結果だけ得る
# 結果が得られない場合はパディングオラクル攻撃は成り立たない
def blackbox(c, iv):
    return aescbc.check_padding(c, iv)

def main():
    # IV + 暗号文
    c = sys.argv[1]
    print "encrypt: ", c
    c = c.decode('hex')

    # ブロックサイズ(16)
    blksz = aescbc.block_size;

    # ブロック数(IV含む)
    blknum = len(c) / blksz
    print "blknum : ", blknum

    m = ""

    # blk = blknum, blknum-1, ..., 2
    for blk in range(blknum, 1, -1):

        # blk番目の暗号ブロック
        c_ = c[blksz * (blk-1) : blksz * blk]
        iv = "";
        prev = "";

        # j = 0, 1, ..., 15
        for j in range(blksz):

            # i = 0, 1, ..., 255
            for i in range(256):

                # c_の復号結果が、j+1バイトだけパディングされたブロックとなるようなivを探索
                # 例）j=0なら、ivの最終1バイトを00-ffで変化させて、c_の復号結果の最終1バイトが'01'となるようなivを探す
                iv = ("00" * (blksz - j - 1)).decode('hex') + chr(i) + prev

                # c_を復号し、復号結果が正しいパディングであるとTrueが返る
                if blackbox(c_, iv):
                    #print iv.encode('hex')
                    prev = ""

                    # ivの最終バイトを、iv_に取り出す (j=0なら、最終1バイト)
                    iv_ = iv[blksz - (j + 1):]
                    for k in range(j + 1):
                        # 次の探索のための準備
                        # j=0なら、c_の復号結果の最終1バイトが'02'となるようにivの最終バイトを調整しておく
                        val = ord(iv_[k])
                        val ^= j + 1
                        val ^= j + 2
                        prev += chr(val)

                    break

        #print "iv     : ", iv.encode('hex')

        # blk番目の平文を得る
        m_ = "";
        for i in range(blksz):
            m_ += chr(0x10 ^ ord(iv[i]) ^ ord(c[blksz * (blk - 2) + i]))

        m = m_ + m

    print "plain  : ", m.encode('hex')

if __name__ == "__main__":
    main()

