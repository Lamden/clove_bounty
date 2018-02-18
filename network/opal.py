from clove.network.bitcoin import Bitcoin


class Opal(Bitcoin):
    """
    Class with all the necessary Opal network information based on
    https://github.com/OpalCoin/OpalCoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'opal'
    symbols = ('OPAL', )
    seeds = ("seed.opal-coin.com",
             "seeder1.opal-coin.com",
             "seeder2.opal-coin.com")
    port = 50990
	
