from clove.network.bitcoin import Bitcoin


class SIGMAcoin(Bitcoin):
    """
    Class with all the necessary SIGMAcoin network information based on
    https://github.com/sigmadevelopment/sigma/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'sigmacoin'
    symbols = ('SIGMA', )
    seeds = ("node.walletbuilders.com")
    port = 8211
	
# no testnet