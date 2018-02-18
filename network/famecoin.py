from clove.network.bitcoin import Bitcoin


class FameCoin(Bitcoin):
    """
    Class with all the necessary FameCoin network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'famecoin'
    symbols = ('FAME', )
    seeds = ("45.77.80.117",
             "45.32.172.67",
             "185.183.99.171",
             "185.183.99.19")
    port = 52758

# no testnet
	
