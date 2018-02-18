from clove.network.bitcoin import Bitcoin


class Radicalcoin(Bitcoin):
    """
    Class with all the necessary Radicalcoin network information based on
    https://github.com/radicalcoin/RADICAL/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'radicalcoin'
    symbols = ('RADI', )
    seeds = ("5.196.10.57")
    port = 42522
	
# no testnet