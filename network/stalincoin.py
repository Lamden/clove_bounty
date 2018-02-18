from clove.network.bitcoin import Bitcoin


class StalinCoin(Bitcoin):
    """
    Class with all the necessary StalinCoin network information based on
    https://github.com/stalincoin/StalinCoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'stalincoin'
    symbols = ('STALIN', )
    seeds = ("seed1.stalincoin.info",
             "seed2.stalincoin.info")
    port = 5422
	
