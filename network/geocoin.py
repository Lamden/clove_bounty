from clove.network.bitcoin import Bitcoin


class GeoCoin(Bitcoin):
    """
    Class with all the necessary GeoCoin network information based on
    https://github.com/doriancoins/doriancoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'geocoin'
    symbols = ('GEO', )
    seeds = ("dnsseed.doriancointools.com",
             "dnsseed.doriancoinpool.org",
             "dnsseed.ltc.xurious.com",
             "dnsseed.koin-project.com",
             "dnsseed.weminemnc.com")	
    port = 1949
	
   
class GeoCoinTestNet(GeoCoin):
    """
    Class with all the necessary GeoCoin testing network information based on
    https://github.com/doriancoins/doriancoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'test-geocoin'
    seeds = ("testnet-seed.doriancointools.com",
             "testnet-seed.weminemnc.com")
    port = 11949               
	
	
