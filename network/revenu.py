from clove.network.bitcoin import Bitcoin


class Revenu(Bitcoin):
    """
    Class with all the necessary Revenu network information based on
    https://github.com/Revenu/revenu-source/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'revenu'
    symbols = ('REV', )
    seeds = ("node.walletbuilders.com")
    port = 6411
	
# no testnet