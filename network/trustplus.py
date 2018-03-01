from clove.network.bitcoin import Bitcoin


class TrustPlus(Bitcoin):
    """
    Class with all the necessary  TrustPlus (TRUST) network information based on
    https://github.com/TrustPlus/TrustPlus/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'trustplus'
    symbols = ('TRUST', )
    seeds = ('104.197.97.72', '23.251.149.70')
    port = 36999


class TrustPlusTestNet(TrustPlus):
    """
    Class with all the necessary  TrustPlus (TRUST) network information based on
    https://github.com/TrustPlus/TrustPlus/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-trustplus'
    symbols = ('TRUST', )
    seeds = ()
    port = 37000
