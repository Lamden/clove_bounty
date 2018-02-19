from clove.network.bitcoin import Bitcoin


class Washingtoncoin(Bitcoin):
    """
    Class with all the necessary Washingtoncoin network information based on
    https://github.com/washingtoncoin/WashingtonCoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'washingtoncoin'
    symbols = ('WASH', )
    seeds = ("45.42.140.30",
             "84.200.210.130")
    port = 15150
	
   
