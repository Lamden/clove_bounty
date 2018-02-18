from clove.network.bitcoin import Bitcoin


class Infinitecoin(Bitcoin):
    """
    Class with all the necessary Infinitecoin network information based on
    https://github.com/infinitecoin/infinitecoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'infinitecoin'
    symbols = ('IFC', )
    seeds = ("dnsseed.infinitecoinpool.org",
             "dnsseed.bytesized-vps.com",
             "dnsseed.ltc.xurious.com")
    port = 9321
	
   
