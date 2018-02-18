from clove.network.bitcoin import Bitcoin


class HealthyWormCoin(Bitcoin):
    """
    Class with all the necessary HealthyWormCoin network information based on
    https://github.com/HealthyWormDotCom/HealthyWorm/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'healthywormcoin'
    symbols = ('WORM', )
    seeds = ("98.144.161.18",
             "164.132.189.192",
             "worm.healthyworm.com")
    port = 8064
	
