
from clove.network.bitcoin import Bitcoin


class SwagBucks(Bitcoin):
    """
    Class with all the necessary BUCKS network information based on
    http://www.github.com/pinkmagicdev/SwagBucks/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'swagbucks'
    symbols = ('BUCKS', )
    seeds = ('', '')
    port = 1337


class SwagBucksTestNet(SwagBucks):
    """
    Class with all the necessary BUCKS testing network information based on
    http://www.github.com/pinkmagicdev/SwagBucks/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-swagbucks'
    seeds = ()
    port = 2337
