from clove.network.bitcoin import Bitcoin


class Xiaomicoin(Bitcoin):
    """
    Class with all the necessary Xiaomicoin network information based on
    https://github.com/xiaomicoin/Xiaomicoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'xiaomicoin'
    symbols = ('MI', )
    seeds = ("120.25.158.22",
             "121.42.12.176")
    port = 27896
	
# no testnet

