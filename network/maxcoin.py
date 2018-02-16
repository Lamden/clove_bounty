from clove.network.bitcoin import Bitcoin


class MaxCoin(Bitcoin):
    """
    Class with all the necessary MaxCoin network information based on
    https://github.com/Max-Coin/maxcoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'maxcoin'
    symbols = ('MAX', )
    seeds = ("a.seed.maxcoinproject.net",
             "b.seed.maxcoinproject.net")
    port = 8668
	
