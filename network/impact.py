from clove.network.bitcoin import Bitcoin


class Impact(Bitcoin):
    """
    Class with all the necessary Impact network information based on
    https://github.com/Impactcoin/Impactcoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'impact'
    symbols = ('IMX', )
    seeds = ("194.135.85.185")
    port = 17771
	
# no testnet