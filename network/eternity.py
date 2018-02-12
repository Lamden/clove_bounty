
from clove.network.bitcoin import Bitcoin


class Eternity(Bitcoin):
    """
    Class with all the necessary ENT network information based on
    http://www.github.com/eternity-group/eternity/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'eternity'
    symbols = ('ENT', )
    seeds = ('dnsseed.eternity-group.org',)
    port = 4855


class EternityTestNet(Eternity):
    """
    Class with all the necessary ENT testing network information based on
    http://www.github.com/eternity-group/eternity/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-eternity'
    seeds = ('144.76.33.134',)
    port = 14855
