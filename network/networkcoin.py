from clove.network.bitcoin import Bitcoin


class Networkcoin(Bitcoin):
    """
    Class with all the necessary Networkcoin network information based on
    https://github.com/NETWORKCOIN/NETC-NETWORKCOINX_13/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'networkcoin'
    symbols = ('NETC', )
    seeds = ("45.63.5.183")
    port = 19172
	
# no testnet