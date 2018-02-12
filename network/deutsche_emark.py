
from clove.network.bitcoin import Bitcoin


class DeutscheeMark(Bitcoin):
    """
    Class with all the necessary DEM network information based on
    http://www.github.com/emarkproject/eMark/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'deutsche-emark'
    symbols = ('DEM', )
    seeds = ('seed.deutsche-emark.de',)
    port = 5556


class DeutscheeMarkTestNet(DeutscheeMark):
    """
    Class with all the necessary DEM testing network information based on
    http://www.github.com/emarkproject/eMark/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-deutsche-emark'
    seeds = ()
    port = 15556
