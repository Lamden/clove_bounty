from clove.network.bitcoin import Bitcoin


class FistBump(Bitcoin):
    """
    Class with all the necessary FistBump network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'fistbump'
    symbols = ('FIST', )
    seeds = ("104.219.53.59")
    port = 13337
	
# No testnet