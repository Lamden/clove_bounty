from clove.network.bitcoin import Bitcoin


class Goacoin(Bitcoin):
    """
    Class with all the necessary Goacoin network information based on
    https://github.com/goacoincore/goacoin/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'goacoin'
    symbols = ('GOA', )
    seeds = ("seed1.goaco.in",
             "seed2.goaco.in",
             "seed3.goaco.in",
             "seed4.goaco.in")
    port = 1947
	
# no testnet