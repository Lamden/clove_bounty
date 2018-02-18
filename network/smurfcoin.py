from clove.network.bitcoin import Bitcoin


class SmurfCoin(Bitcoin):
    """
    Class with all the necessary SmurfCoin network information based on
    https://github.com/smurfscoin/smf/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'smurfcoin'
    symbols = ('SMF', )
    seeds = ("45.55.83.96")
    port = 43221
	
# no testnet