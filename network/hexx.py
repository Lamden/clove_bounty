
from clove.network.bitcoin import Bitcoin


class Hexx(Bitcoin):
    """
    Class with all the necessary HXX network information based on
    http://www.github.com/hexxcointakeover/hexxcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'hexx'
    symbols = ('HXX', )
    seeds = ('76.74.170.249',)
    port = 29100


class HexxTestNet(Hexx):
    """
    Class with all the necessary HXX testing network information based on
    http://www.github.com/hexxcointakeover/hexxcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-hexx'
    seeds = ()
    port = 29101
