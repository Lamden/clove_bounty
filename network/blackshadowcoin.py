from clove.network.bitcoin import Bitcoin


class BlackShadowCoin(Bitcoin):
    """
    Class with all the necessary BlackShadowCoin network information based on
    https://github.com/blackshadowcoin/bs/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'blackshadowcoin'
    symbols = ('BS', )
    seeds =  ("198.199.90.93")
    port = 48221
	
# Has no testnet