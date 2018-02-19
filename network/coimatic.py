from clove.network.bitcoin import Bitcoin


class Coimatic30(Bitcoin):
    """
    Class with all the necessary Coimatic 3.0 network information based on
    https://github.com/coimatic/coimatic-master/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'Coimatic30'
    symbols = ('CTIC3', )
    seeds = ("94.176.235.210",
             "94.176.235.203")
    port = 34222
	
# no testnet