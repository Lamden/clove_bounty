from clove.network.bitcoin import Bitcoin


class Aces(Bitcoin):
    """
    Class with all the necessary  Aces (ACES) network information based on
    https://github.com/aces-coin/AcesCoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'aces'
    symbols = ('ACES', )
    seeds = ('81.4.123.155')
    port = 21274


class AcesTestNet(Aces):
    """
    Class with all the necessary  Aces (ACES) network information based on
    https://github.com/aces-coin/AcesCoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-aces'
    symbols = ('ACES', )
    seeds = ()
    port = 21275
