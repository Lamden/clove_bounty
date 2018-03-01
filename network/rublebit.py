from clove.network.bitcoin import Bitcoin


class RubleBit(Bitcoin):
    """
    Class with all the necessary RubleBit network information based on
    https://github.com/rublebit/rublebit/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'rublebit'
    symbols = ('RUBIT', )
    seeds = ("128.199.38.11")
    port = 11333


class RubleBitTestNet(RubleBit):
    """
    Class with all the necessary RubleBit testing network information based on
    https://github.com/rublebit/rublebit/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-rublebit'
    seeds = ("testnet-seed.ltc.xurious.com",
             "dnsseed.wemine-testnet.com")
    port = 11333
