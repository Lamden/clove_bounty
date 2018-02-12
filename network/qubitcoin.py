
from clove.network.bitcoin import Bitcoin


class QubitCoin(Bitcoin):
    """
    Class with all the necessary Q2C network information based on
    http://www.github.com/willowrose/QubitCoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'qubitcoin'
    symbols = ('Q2C', )
    seeds = ('q2c1.ignorelist.com', 'q2c2.ignorelist.com', 'q2c3.ignorelist.com', 'q2c4.ignorelist.com')
    port = 7788


class QubitCoinTestNet(QubitCoin):
    """
    Class with all the necessary Q2C testing network information based on
    http://www.github.com/willowrose/QubitCoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-qubitcoin'
    seeds = ()
    port = 11788
