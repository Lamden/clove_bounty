from clove.network.bitcoin import Bitcoin


class Marscoin(Bitcoin):
    """
    Class with all the necessary Marscoin network information based on
    https://github.com/marscoin/marscoin/blob/master-0.2/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'marscoin'
    symbols = ('MARS', )
    seeds = ("dnsseed.marscoin.ru",
             "dnsseed.marscoin.org",
             "dnsseed.marsbiotech.com")
    port = 8338


class MarscoinTestNet(Marscoin):
    """
    Class with all the necessary Diamond testing network information based on
    https://github.com/marscoin/marscoin/blob/master-0.2/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-marscoin'
    seeds = ("dnsseed.marscoin.ru",
             "testnet-seed.marscointools.com")
    port = 18338
