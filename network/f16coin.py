from clove.network.bitcoin import Bitcoin


class F16Coin(Bitcoin):
    """
    Class with all the necessary F16Coin network information based on
    https://github.com/f16coin/air/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'f16coin'
    symbols = ('F16', )
    seeds = ("node.walletbuilders.com")
    port = 18077
	
# no testnet