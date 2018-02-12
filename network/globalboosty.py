
from clove.network.bitcoin import Bitcoin


class GlobalBoostY(Bitcoin):
    """
    Class with all the necessary BSTY network information based on
    http://www.github.com/GlobalBoost/GlobalBoost-Y/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'globalboosty'
    symbols = ('BSTY', )
    seeds = ('seeder.globalboost.info', 'seeder2.globalboost.info')
    port = 8226


class GlobalBoostYTestNet(GlobalBoostY):
    """
    Class with all the necessary BSTY testing network information based on
    http://www.github.com/GlobalBoost/GlobalBoost-Y/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-globalboost-y'
    seeds = ('testnet-seeder.globalboost.info',)
    port = 18226
