from clove.network.bitcoin import Bitcoin


class Techcoin(Bitcoin):
    """
    Class with all the necessary Techcoin network information based on
    https://github.com/techcoincommunity/techcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'techcoin'
    symbols = ('TECH', )
    seeds = ("24.85.126.229",
             "179.211.40.9",
             "50.188.14.165")
    port = 57697
	
   
