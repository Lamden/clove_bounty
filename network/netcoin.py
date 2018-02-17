from clove.network.bitcoin import Bitcoin


class NetCoin(Bitcoin):
    """
    Class with all the necessary NetCoin network information based on
    https://github.com/netcoinfoundation/netcoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'netcoin'
    symbols = ('NET', )
    seeds = ("netseed.presstab.pw")
    port = 11310
	
# no testnet