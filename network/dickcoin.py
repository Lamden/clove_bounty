from clove.network.bitcoin import Bitcoin


class DickCoin(Bitcoin):
    """
    Class with all the necessary DickCoin network information based on
    https://github.com/DickCoin/Source/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'dickcoin'
    symbols = ('DCK', )
    seeds = ("seed1.cryptolife.net",
             "seed2.cryptolife.net",
             "seed3.cryptolife.net",
             "electrum1.cryptolife.net",
             "wallet.cryptolife.net",
             "explore.cryptolife.net")
    port = 41018
	
# Has no testnet
	