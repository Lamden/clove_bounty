
from clove.network.bitcoin import Bitcoin


class LeaCoin(Bitcoin):
    """
    Class with all the necessary LEA network information based on
    http://www.github.com/leacoin/LeaCoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'leacoin'
    symbols = ('LEA', )
    seeds = ('dnsseed.leacoin.org',)
    port = 18123


class LeaCoinTestNet(LeaCoin):
    """
    Class with all the necessary LEA testing network information based on
    http://www.github.com/leacoin/LeaCoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-leacoin'
    seeds = ('test.leacoin.org',)
    port = 55534
