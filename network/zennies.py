
from clove.network.bitcoin import Bitcoin


class Zennies(Bitcoin):
    """
    Class with all the necessary ZENI network information based on
    http://www.github.com/zennies/zennies/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'zennies'
    symbols = ('ZENI', )
    seeds = ('54.214.213.181', '54.186.147.219', '91.134.120.210', 'east1.zeni.zone', 'west1.zeni.zone')
    port = 11011


class ZenniesTestNet(Zennies):
    """
    Class with all the necessary ZENI testing network information based on
    http://www.github.com/zennies/zennies/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-zennies'
    seeds = ()
    port = 11021
