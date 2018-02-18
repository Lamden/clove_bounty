from clove.network.bitcoin import Bitcoin


class ShrekCoin(Bitcoin):
    """
    Class with all the necessary ShrekCoin network information based on
    https://github.com/shrekcoin/shrek/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'shrekcoin'
    symbols = ('SHREK', )
    seeds = ("node.walletbuilders.com")
    port = 7443
	
# no testnet