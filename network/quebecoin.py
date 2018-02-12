
from clove.network.bitcoin import Bitcoin


class Quebecoin(Bitcoin):
    """
    Class with all the necessary QBC network information based on
    http://www.github.com/jpgagnon/qbc/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'quebecoin'
    symbols = ('QBC', )
    seeds = ('dnsseed.qbc.io', '54.86.39.92')
    port = 56790


class QuebecoinTestNet(Quebecoin):
    """
    Class with all the necessary QBC testing network information based on
    http://www.github.com/jpgagnon/qbc/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-quebecoin'
    seeds = ('testnet-seed.qbc.io',)
    port = 46790
