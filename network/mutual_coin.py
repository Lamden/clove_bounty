from clove.network.bitcoin import Bitcoin


class Mutual_Coin(Bitcoin):
    """
    Class with all the necessary Mutual_Coin network information based on
    https://github.com/MutualCoin/MutualCoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'mutual_coin'
    symbols = ('MUT', )
    seeds = ("mut1.mywire.org",
             "mut2.mywire.org")
    port = 25731
	
