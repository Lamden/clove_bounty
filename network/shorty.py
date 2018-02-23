from clove.network.bitcoin import Bitcoin


class Shorty(Bitcoin):
    """
    Class with all the necessary Shorty network information based on
    https://github.com/shortysho/shorty/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'shorty'
    symbols = ('SHORTY', )
    seeds = ("35.163.38.207")
    port = 28188
	
# no testnet