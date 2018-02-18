from clove.network.bitcoin import Bitcoin


class Vectorcoin(Bitcoin):
    """
    Class with all the necessary Vectorcoin network information based on
    https://github.com/vectorcoin/vectorcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'vectorcoin'
    symbols = ('VEC', )
    seeds = ("dnsseed.litecointools.com",
             "dnsseed.litecoinpool.org",
             "dnsseed.ltc.xurious.com",
             "dnsseed.koin-project.com",
             "dnsseed.weminemnc.com")
    port = 55333
	
   
class VectorcoinTestNet(Vectorcoin):
    """
    Class with all the necessary Vectorcoin testing network information based on
    https://github.com/vectorcoin/vectorcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-vectorcoin'
    seeds = ("testnet-seed.litecointools.com",
             "testnet-seed.ltc.xurious.com",
             "dnsseed.wemine-testnet.com")
    port = 55444              