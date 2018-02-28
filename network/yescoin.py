
from clove.network.bitcoin import Bitcoin


class Yescoin(Bitcoin):
    """
    Class with all the necessary YES network information based on
    http://www.github.com/yescoindev/yes/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'yescoin'
    symbols = ('YES', )
    seeds = ('seed.yescoin.us', 'seed2.yescoin.us',
             'seed3.yescoin.us', 'seed4.yescoin.us', 'seed.yescoin.us')
    port = 4444


class YescoinTestNet(Yescoin):
    """
    Class with all the necessary YES testing network information based on
    http://www.github.com/yescoindev/yes/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-yescoin'
    seeds = ()
    port = 51997
