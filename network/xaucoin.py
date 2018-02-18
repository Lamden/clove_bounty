from clove.network.bitcoin import Bitcoin


class Xaucoin(Bitcoin):
    """
    Class with all the necessary Xaucoin network information based on
    https://github.com/tuaris/xaucoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'xaucoin'
    symbols = ('XAU', )
    seeds = ("xaucoin.ddns.net")
    port = 11063
	
# no testnet