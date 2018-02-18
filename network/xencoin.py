from clove.network.bitcoin import Bitcoin


class XenCoin(Bitcoin):
    """
    Class with all the necessary XenCoin network information based on
    https://github.com/xencoin/Xencoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'xencoin'
    symbols = ('XNC', )
    seeds = ("192.241.131.40")
    port = 4334
	
# no testnet