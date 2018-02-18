from clove.network.bitcoin import Bitcoin


class BigCoin(Bitcoin):
    """
    Class with all the necessary BigCoin network information based on
    https://github.com/bigcoin/bigcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bigcoin'
    symbols = ('HUGE', )
    seeds =  ("bigcoin.org")
    port = 55884
	
# Has no testnet