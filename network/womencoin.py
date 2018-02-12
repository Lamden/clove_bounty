
from clove.network.bitcoin import Bitcoin


class WomenCoin(Bitcoin):
    """
    Class with all the necessary WOMEN network information based on
    https://github.com/womencoin/womencoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'womencoin'
    symbols = ('WOMEN', )
    seeds = ('104.200.67.104')
    port = 19207


class WomenCoinTestNet(WomenCoin):
    """
    Class with all the necessary WOMEN testing network information based on
    https://github.com/womencoin/womencoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-womencoin'
    seeds = ()
    port = 29207