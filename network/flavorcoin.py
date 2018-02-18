from clove.network.bitcoin import Bitcoin


class FlavorCoin(Bitcoin):
    """
    Class with all the necessary FlavorCoin network information based on
    https://github.com/flavorcoin/FlavorCoin-V2/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'flavorcoin'
    symbols = ('FLVR', )
    seeds = ("2flav.nodes.altcoinsteps.com")
    port = 17771
	
# No testnet