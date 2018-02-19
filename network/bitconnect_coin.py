from clove.network.bitcoin import Bitcoin


class Bitconnect_Coin(Bitcoin):
    """
    Class with all the necessary Bitconnect_Coin network information based on
    https://github.com/bitconnectcoin/bitconnectcoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'bitconnect_coin'
    symbols = ('BCCOIN', )
    seeds = ("198.211.115.116")
    port = 9239
	
# no testnet