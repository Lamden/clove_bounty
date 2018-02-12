
from clove.network.bitcoin import Bitcoin


class Bitok(Bitcoin):
    """
    Class with all the necessary BITOK network information based on
    http://www.github.com/bitokproject/bitok/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'bitok'
    symbols = ('BITOK', )
    seeds = ('seed.bitok.online', 'seed2.bitok.online', 'seed3.bitok.online')
    port = 11122


class BitokTestNet(Bitok):
    """
    Class with all the necessary BITOK testing network information based on
    http://www.github.com/bitokproject/bitok/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-bitok'
    seeds = ()
    port = 21997
