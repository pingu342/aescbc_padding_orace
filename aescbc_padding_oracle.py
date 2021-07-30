#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from Crypto.Cipher import AES
import aescbc

# $B0E9fJ8$rI|9f$7%Q%G%#%s%0$,@5$7$1$l$P(BTrue$B$rJV$9(B
# $B967b$9$kB&$O(Bkey$B$rCN$i$J$$(B
# $B$=$3$G967b$5$l$kB&$KI|9f$5$;$F@5$7$/I|9f$G$-$?$+$I$&$+$N7k2L$@$1F@$k(B
# $B7k2L$,F@$i$l$J$$>l9g$O%Q%G%#%s%0%*%i%/%k967b$O@.$jN)$?$J$$(B
def blackbox(c, iv):
    return aescbc.check_padding(c, iv)

def main():
    # IV + $B0E9fJ8(B
    c = sys.argv[1]
    print "encrypt: ", c
    c = c.decode('hex')

    # $B%V%m%C%/%5%$%:(B(16)
    blksz = aescbc.block_size;

    # $B%V%m%C%/?t(B(IV$B4^$`(B)
    blknum = len(c) / blksz
    print "blknum : ", blknum

    m = ""

    # blk = blknum, blknum-1, ..., 2
    for blk in range(blknum, 1, -1):

        # blk$BHVL\$N0E9f%V%m%C%/(B
        c_ = c[blksz * (blk-1) : blksz * blk]
        iv = "";
        prev = "";

        # j = 0, 1, ..., 15
        for j in range(blksz):

            # i = 0, 1, ..., 255
            for i in range(256):

                # c_$B$NI|9f7k2L$,!"(Bj+1$B%P%$%H$@$1%Q%G%#%s%0$5$l$?%V%m%C%/$H$J$k$h$&$J(Biv$B$rC5:w(B
                # $BNc!K(Bj=0$B$J$i!"(Biv$B$N:G=*(B1$B%P%$%H$r(B00-ff$B$GJQ2=$5$;$F!"(Bc_$B$NI|9f7k2L$N:G=*(B1$B%P%$%H$,(B'01'$B$H$J$k$h$&$J(Biv$B$rC5$9(B
                iv = ("00" * (blksz - j - 1)).decode('hex') + chr(i) + prev

                # c_$B$rI|9f$7!"I|9f7k2L$,@5$7$$%Q%G%#%s%0$G$"$k$H(BTrue$B$,JV$k(B
                if blackbox(c_, iv):
                    #print iv.encode('hex')
                    prev = ""

                    # iv$B$N:G=*%P%$%H$r!"(Biv_$B$K<h$j=P$9(B (j=0$B$J$i!":G=*(B1$B%P%$%H(B)
                    iv_ = iv[blksz - (j + 1):]
                    for k in range(j + 1):
                        # $B<!$NC5:w$N$?$a$N=`Hw(B
                        # j=0$B$J$i!"(Bc_$B$NI|9f7k2L$N:G=*(B1$B%P%$%H$,(B'02'$B$H$J$k$h$&$K(Biv$B$N:G=*%P%$%H$rD4@0$7$F$*$/(B
                        val = ord(iv_[k])
                        val ^= j + 1
                        val ^= j + 2
                        prev += chr(val)

                    break

        #print "iv     : ", iv.encode('hex')

        # blk$BHVL\$NJ?J8$rF@$k(B
        m_ = "";
        for i in range(blksz):
            m_ += chr(0x10 ^ ord(iv[i]) ^ ord(c[blksz * (blk - 2) + i]))

        m = m_ + m

    print "plain  : ", m.encode('hex')

if __name__ == "__main__":
    main()

