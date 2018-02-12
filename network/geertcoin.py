
from clove.network.bitcoin import Bitcoin


class GeertCoin(Bitcoin):
    """
    Class with all the necessary GEERT network information based on
    http://www.github.com/GeertAltCoin/Geertcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'geertcoin'
    symbols = ('GEERT', )
    seeds = ('dnsseed.geertcoin.com',)
    port = 64333


class GeertCoinTestNet(GeertCoin):
    """
    Class with all the necessary GEERT testing network information based on
    http://www.github.com/GeertAltCoin/Geertcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-geertcoin'
    seeds = ('testnet-seed.geertcoin.com',)
    port = 65333
