from clove.network.bitcoin import Bitcoin


class BlackCoin(Bitcoin):
    """
    Class with all the necessary BlackCoin network information based on
    https://github.com/CoinBlack/blackcoin/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'BlackCoin'
    symbols = ('BLK', )
    seeds =  ("dnsseed.vasin.nl")
    port = 15714
	
# Has no testnet