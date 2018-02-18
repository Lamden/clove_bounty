from clove.network.bitcoin import Bitcoin


class Silkcoin(Bitcoin):
    """
    Class with all the necessary Silkcoin network information based on
    https://github.com/shnurf/silkcoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'silkcoin'
    symbols = ('SILK', )
    seeds = ("107.170.61.197","107.170.73.238")
    port = 16666
	
# no testnet