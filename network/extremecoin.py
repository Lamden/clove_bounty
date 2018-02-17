from clove.network.bitcoin import Bitcoin


class Extremecoin(Bitcoin):
    """
    Class with all the necessary Extremecoin network information based on
    https://github.com/CaptChadd/Extremecoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'extremecoin'
    symbols = ('EXC', )
    seeds = ("212.48.67.126")
    port = 26667
	
# No testnet