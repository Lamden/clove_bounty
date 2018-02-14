from clove.network.bitcoin import Bitcoin


class BeachCoin(Bitcoin):
    """
    Class with all the necessary BeachCoin network information based on
    https://github.com/beachcoinorg/wallets/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'beachcoin'
    symbols = ('SAND', )
    seeds = ("seed5.cryptolife.net",
             "seed6.cryptolife.net",
             "seed3.cryptolife.net",
             "electrum6.cryptolife.net")
    port = 17771
	
# Has no testnet

