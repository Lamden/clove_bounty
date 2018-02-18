from clove.network.bitcoin import Bitcoin


class GlobalBoost(Bitcoin):
    """
    Class with all the necessary GlobalBoost network information based on
    https://github.com/GlobalBoost/GlobalBoost-Y/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'globalboost'
    symbols = ('BSTY', )
    seeds = ("seeder.globalboost.info","seeder2.globalboost.info")
    port = 8226
	
   
class GlobalBoostTestNet(GlobalBoost):
    """
    Class with all the necessary GlobalBoost testing network information based on
    https://github.com/GlobalBoost/GlobalBoost-Y/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-globalboost'
    seeds = ("testnet-seeder.globalboost.info")
    port = 18226              