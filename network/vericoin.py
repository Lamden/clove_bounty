
from clove.network.bitcoin import Bitcoin


class VeriCoin(Bitcoin):
    """
    Class with all the necessary VRC network information based on
    https://github.com/vericoin/vericoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'vericoin'
    symbols = ('VRC', )
    seeds = ('dnsseed.vericoin.info')
    port = 58684


class VeriCoinTestNet(VeriCoin):
    """
    Class with all the necessary VRC testing network information based on
    https://github.com/vericoin/vericoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-vericoin'
    seeds = ()
    port = 48684