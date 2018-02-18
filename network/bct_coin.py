from clove.network.bitcoin import Bitcoin


class BCT_Coin(Bitcoin):
    """
    Class with all the necessary BCT Coin network information based on
    https://github.com/bctc/bctcoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'bct_coin'
    symbols = ('BCT', )
    seeds = ("208.167.233.222",
             "76.74.178.182",
             "69.90.132.171")
    port = 2455
	
   
class BCT_CoinTestNet(BCT_Coin):
    """
    Class with all the necessary BCT Coin testing network information based on
    https://github.com/bctc/bctcoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-bct_coin'
    seeds = ("208.167.233.222",
             "76.74.178.182",
             "69.90.132.171")
    port = 12455               
	
