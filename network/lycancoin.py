from clove.network.bitcoin import Bitcoin


class Lycancoin(Bitcoin):
    """
    Class with all the necessary Lycancoin network information based on
    https://github.com/lycancoin/lycancoin-release/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'lycancoin'
    symbols = ('LYC', )
    seeds = ("69.172.229.161","209.208.111.72")
    port = 58862
	
