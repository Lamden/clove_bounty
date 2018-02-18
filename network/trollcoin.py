from clove.network.bitcoin import Bitcoin


class Trollcoin(Bitcoin):
    """
    Class with all the necessary Trollcoin network information based on
    https://github.com/TrollCoin2/TrollCoin-2.0/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'trollcoin'
    symbols = ('TROLL', )
    seeds = ("dnsfeed.trollcoin.com",
             "dnsfeed.trollcoinbase.com")	
    port = 15000
	
# no testnet