from clove.network.bitcoin import Bitcoin


class MilkCoin(Bitcoin):
    """
    Class with all the necessary MilkCoin network information based on
    https://github.com/milkcoin/milk/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'milkcoin'
    symbols = ('MUU', )
    seeds = ("185.69.55.50")
    port = 35235
	
# no testnet