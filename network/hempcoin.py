from clove.network.bitcoin import Bitcoin


class HempCoin(Bitcoin):
    """
    Class with all the necessary HempCoin network information based on
    https://github.com/hempcoin-project/THC/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'hempcoin'
    symbols = ('THC', )
    seeds = ("162.243.1.45")
    port = 21054
	
# no testnet