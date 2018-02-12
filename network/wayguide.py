
from clove.network.bitcoin import Bitcoin


class WayGuide(Bitcoin):
    """
    Class with all the necessary WAY network information based on
    https://github.com/wayguide/waycoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'wayguide'
    symbols = ('WAY', )
    seeds = ()
    port = 21000


class WayGuideTestNet(WayGuide):
    """
    Class with all the necessary WAY testing network information based on
    https://github.com/wayguide/waycoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-wayguide'
    seeds = ()
    port = 22000