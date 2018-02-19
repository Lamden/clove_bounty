from clove.network.bitcoin import Bitcoin


class ZCashDarkCoin(Bitcoin):
    """
    Class with all the necessary ZCashDarkCoin network information based on
    https://github.com/zcashdarkcoin/zcashdark/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'zcashdarkcoin'
    symbols = ('ZEC', )
    seeds = ("162.243.1.45")
    port = 7785
	
# no testnet