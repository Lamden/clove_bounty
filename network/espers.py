
from clove.network.bitcoin import Bitcoin


class Espers(Bitcoin):
    """
    Class with all the necessary ESP network information based on
    http://www.github.com/cryptocoderz/espers/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'espers'
    symbols = ('ESP', )
    seeds = ('esp.cryptocoderz.com',)
    port = 22448


class EspersTestNet(Espers):
    """
    Class with all the necessary ESP testing network information based on
    http://www.github.com/cryptocoderz/espers/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-espers'
    seeds = ()
    port = 32448
