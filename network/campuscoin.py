
from clove.network.bitcoin import Bitcoin


class CampusCoin(Bitcoin):
    """
    Class with all the necessary CMPCO network information based on
    http://www.github.com/campuscoindev/CampusCoin-Source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'campuscoin'
    symbols = ('CMPCO', )
    seeds = ('seed5.cryptolife.net', 'seed6.cryptolife.net')
    port = 28195


class CampusCoinTestNet(CampusCoin):
    """
    Class with all the necessary CMPCO testing network information based on
    http://www.github.com/campuscoindev/CampusCoin-Source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-campuscoin'
    seeds = ()
    port = 33813
