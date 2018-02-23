from clove.network.bitcoin import Bitcoin


class Nerdcoin(Bitcoin):
    """
    Class with all the necessary Nerdcoin network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/21/2018)
    """
    name = 'nerdcoin'
    symbols = ('NERD', )
    seeds = ("45.55.148.6")
    port = 31338
	
# no testnet