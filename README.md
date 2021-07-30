# aescbc_padding_oracle

平文 "hello world" を暗号化する。鍵、IVは固定。

    $ python aescbc.py "hello world"
    plain  :  68656c6c6f20776f726c64
    padding:  68656c6c6f20776f726c640505050505
    key    :  0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a
    iv     :  495620666f7220434243206d6f64652e
    encrypt:  495620666f7220434243206d6f64652e5a33ba397d03b6f73356f690f101e832
    decrypt:  68656c6c6f20776f726c640505050505
    valid  :  True
    plain  :  68656c6c6f20776f726c64

パディングオラクル攻撃によって復号する。
上記結果のencrypt:の行（IV、暗号文を連結した値）を入力とする。

    $ python aescbc_padding_oracle.py 495620666f7220434243206d6f64652e5a33ba397d03b6f73356f690f101e832
    encrypt:  495620666f7220434243206d6f64652e5a33ba397d03b6f73356f690f101e832
    blknum :  2
    plain  :  68656c6c6f20776f726c640505050505
    iv     :  495620666f7220434243206d6f64652e

平文とIVが判明する。（平文にはパディングが含まれている）
