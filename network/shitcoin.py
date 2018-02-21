from clove.network.bitcoin import Bitcoin


class Shitcoin(Bitcoin):
    """
    Class with all the necessary Shitcoin network information based on
    https://github.com/shit-coin/shit/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'shitcoin'
    symbols = ('SHIT', )
    seeds = ("172.245.173.137")
    port = 9999
	
# no testnet