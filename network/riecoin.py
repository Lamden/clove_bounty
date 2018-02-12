
from clove.network.bitcoin import Bitcoin


class Riecoin(Bitcoin):
    """
    Class with all the necessary RIC network information based on
    http://www.github.com/riecoin/riecoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'riecoin'
    symbols = ('RIC', )
    seeds = ('seed.bitcoin.sipa.be',)
    port = 28333


class RiecoinTestNet(Riecoin):
    """
    Class with all the necessary RIC testing network information based on
    http://www.github.com/riecoin/riecoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-riecoin'
    seeds = ()
    port = 38333
