
from clove.network.bitcoin import Bitcoin


class Opescoin(Bitcoin):
    """
    Class with all the necessary OPES network information based on
    http://www.github.com/OpesCoin/OPES/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'opescoin'
    symbols = ('OPES', )
    seeds = ('104.218.50.15',)
    port = 6222


class OpescoinTestNet(Opescoin):
    """
    Class with all the necessary OPES testing network information based on
    http://www.github.com/OpesCoin/OPES/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-opescoin'
    seeds = ('dnsseed.OPES.org',)
    port = 26222
