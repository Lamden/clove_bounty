
from clove.network.bitcoin import Bitcoin


class BlazeCoin(Bitcoin):
    """
    Class with all the necessary BLZ network information based on
    http://www.github.com/wpstudio/blazecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'blazecoin'
    symbols = ('BLZ', )
    seeds = ('172.245.137.35',)
    port = 55414


class BlazeCoinTestNet(BlazeCoin):
    """
    Class with all the necessary BLZ testing network information based on
    http://www.github.com/wpstudio/blazecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-blazecoin'
    seeds = ('testnet.seedtest.blazeco.in',)
    port = 75414
