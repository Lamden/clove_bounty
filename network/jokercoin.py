from clove.network.bitcoin import Bitcoin


class JokerCoin(Bitcoin):
    """
    Class with all the necessary JokerCoin network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'jokercoin'
    symbols = ('JOK', )
    seeds = ("45.55.83.96")
    port = 32880 
	
# No testnet