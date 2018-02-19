from clove.network.bitcoin import Bitcoin


class WarCoin(Bitcoin):
    """
    Class with all the necessary WarCoin network information based on
    https://github.com/warcoindev/WarCoin/blob/master/warcoin-source/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'warcoin'
    symbols = ('WRC', )
    seeds = ("node.walletbuilders.com")
    port = 10395
	
# no testnet