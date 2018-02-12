
from clove.network.bitcoin import Bitcoin


class InsaneCoin(Bitcoin):
    """
    Class with all the necessary INSN network information based on
    http://www.github.com/CryptoCoderz/INSN/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'insanecoin'
    symbols = ('INSN', )
    seeds = ('insn.cryptocoderz.com', 'insane.cryptocoderz.com', '195.74.52.227')
    port = 10255


class InsaneCoinTestNet(InsaneCoin):
    """
    Class with all the necessary INSN testing network information based on
    http://www.github.com/CryptoCoderz/INSN/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-insanecoin'
    seeds = ()
    port = 10260
