
from clove.network.bitcoin import Bitcoin


class Diamond(Bitcoin):
    """
    Class with all the necessary DMD network information based on
    http://www.github.com/DMDcoin/Diamond/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'diamond'
    symbols = ('DMD', )
    seeds = ('dnsseed.bit.diamonds', '37.120.186.85', '185.194.140.60', '188.68.39.1', '188.68.52.172')
    port = 17771


class DiamondTestNet(Diamond):
    """
    Class with all the necessary DMD testing network information based on
    http://www.github.com/DMDcoin/Diamond/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-diamond'
    seeds = ('dnsseed.bit.diamonds',)
    port = 51474
