from clove.network.bitcoin import Bitcoin


class Zeta2Coin(Bitcoin):
    """
    Class with all the necessary Zeta2Coin network information based on
    https://github.com/ZETA2COIN/ZETACOIN2-ZET2/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'zeta2coin'
    symbols = ('ZET2', )
    seeds = ("185.61.151.109")
    port = 25589
	
# no testnet