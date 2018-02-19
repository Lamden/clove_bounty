from clove.network.bitcoin import Bitcoin


class Coupecoin(Bitcoin):
    """
    Class with all the necessary Coupecoin network information based on
    https://github.com/CoupecoinOriginal/coupecoin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'coupecoin'
    symbols = ('COUPE', )
    seeds = ("45.79.66.198",
             "electrum5.cryptolife.net")
    port = 17739
	
