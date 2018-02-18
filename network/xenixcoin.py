from clove.network.bitcoin import Bitcoin


class Xenixcoin(Bitcoin):
    """
    Class with all the necessary Xenixcoin network information based on
    https://github.com/xenixcoin/xenixcoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'xenixcoin'
    symbols = ('XEN', )
    seeds = ("92.63.57.235","92.63.57.104")
    port = 5556
	
# no testnet

