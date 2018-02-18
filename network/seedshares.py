from clove.network.bitcoin import Bitcoin


class SeedShares(Bitcoin):
    """
    Class with all the necessary SeedShares network information based on
    https://github.com/SeedShares/SeedShare/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'seedshares'
    symbols = ('SEEDS', )
    seeds = ("107.170.238.71")
    port = 32231
	
# no testnet