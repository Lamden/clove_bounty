from clove.network.bitcoin import Bitcoin


class Pentacoin(Bitcoin):
    """
    Class with all the necessary Pentacoin network information based on
    https://github.com/penta2015/pentacoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'pentacoin'
    symbols = ('PTA', )
    seeds = ("104.236.199.148")
    port = 25631
	
# no testnet