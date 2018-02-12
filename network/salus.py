
from clove.network.bitcoin import Bitcoin


class SaluS(Bitcoin):
    """
    Class with all the necessary SLS network information based on
    http://www.github.com/saluscoin/SaluS/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'salus'
    symbols = ('SLS', )
    seeds = ('198.50.243.69',)
    port = 22534


class SaluSTestNet(SaluS):
    """
    Class with all the necessary SLS testing network information based on
    http://www.github.com/saluscoin/SaluS/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-salus'
    seeds = ()
    port = 55937
