from clove.network.bitcoin import Bitcoin


class Firecoin(Bitcoin):
    """
    Class with all the necessary Firecoin network information based on
    https://github.com/firecoinx/Firecoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'firecoin'
    symbols = ('FIRE', )
    seeds = ("23.254.97.249")
    port = 49697
	
# no testnet