
from clove.network.bitcoin import Bitcoin


class GeyserCoin(Bitcoin):
    """
    Class with all the necessary GSR network information based on
    http://www.github.com/geysercoin/geysercoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'geysercoin'
    symbols = ('GSR', )
    seeds = ('nodea.geysercoin.com', 'nodeb.geysercoin.com', 'nodec.geysercoin.com')
    port = 10556


class GeyserCoinTestNet(GeyserCoin):
    """
    Class with all the necessary GSR testing network information based on
    http://www.github.com/geysercoin/geysercoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-geysercoin'
    seeds = ()
    port = 20556
