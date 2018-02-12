
from clove.network.bitcoin import Bitcoin


class Renos(Bitcoin):
    """
    Class with all the necessary RNS network information based on
    http://www.github.com/RenosCoin/RenosCoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'renos'
    symbols = ('RNS', )
    seeds = ('seed.renoscoin.com', 'seed.renos.network')
    port = 57155


class RenosTestNet(Renos):
    """
    Class with all the necessary RNS testing network information based on
    http://www.github.com/RenosCoin/RenosCoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-renos'
    seeds = ()
    port = 57255
