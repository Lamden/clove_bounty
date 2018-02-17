from clove.network.bitcoin import Bitcoin


class Bithire(Bitcoin):
    """
    Class with all the necessary Bithire network information based on
    https://github.com/Bithire/Bithire/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bithire'
    symbols = ('HIRE', )
    seeds =  ("46.101.3.80")
    port = 11816
	
# Has no testnet