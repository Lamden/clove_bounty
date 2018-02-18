from clove.network.bitcoin import Bitcoin


class WealthCoin(Bitcoin):
    """
    Class with all the necessary WealthCoin network information based on
    https://github.com/WealthCoinDev/WealthCoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'wealthcoin'
    symbols = ('WEALTH', )
    seeds = ("104.236.220.47")
    port = 15152
	
# no testnet