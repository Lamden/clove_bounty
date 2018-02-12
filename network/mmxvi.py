
from clove.network.bitcoin import Bitcoin


class MMXVI(Bitcoin):
    """
    Class with all the necessary MMXVI network information based on
    http://www.github.com/coin2016/MMXVI/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'mmxvi'
    symbols = ('MMXVI', )
    seeds = ('5.196.67.100',)
    port = 6503


class MMXVITestNet(MMXVI):
    """
    Class with all the necessary MMXVI testing network information based on
    http://www.github.com/coin2016/MMXVI/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-mmxvi'
    seeds = ('dnsseed.MMXVI.org',)
    port = 16503
