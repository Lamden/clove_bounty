from clove.network.bitcoin import Bitcoin


class Kobocoin(Bitcoin):
    """
    Class with all the necessary Kobocoin network information based on
    https://github.com/kobocoin/Kobocoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'kobocoin'
    symbols = ('KOBO', )
    seeds = ("dns1.kobocoin.com",
             "dns2.kobocoin.com",
             "dns3.kobocoin.com",
             "dns4.kobocoin.com")
    port = 9011
	
