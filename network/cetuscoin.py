from clove.network.bitcoin import Bitcoin


class Cetuscoin(Bitcoin):
    """
    Class with all the necessary Cetuscoin network information based on
    https://github.com/CetusCoin/Ceti/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'cetuscoin'
    symbols = ('CETI', )
    seeds = ("seed.cetuscoin.cc",
             "seed2.cetuscoin.cc",
             "seed3.cetuscoin.cc")
    port = 24772
	
# no testnet

