from clove.network.bitcoin import Bitcoin


class DavorCoin(Bitcoin):
    """
    Class with all the necessary DavorCoin network information based on
    https://github.com/davorcc/DavorCoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'davorcoin'
    symbols = ('DAV', )
    seeds =  ("52.77.118.10")
    port = 17511
	
# No testnet