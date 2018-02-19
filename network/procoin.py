from clove.network.bitcoin import Bitcoin


class ProCoin(Bitcoin):
    """
    Class with all the necessary ProCoin network information based on
    https://github.com/Procoin-project/Procoin-Done/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'procoin'
    symbols = ('PCN', )
    seeds = ("dnsseed.procointools.com",
             "dnsseed.procoinpool.org",
             "dnsseed.pro.xurious.com",
             "dnsseed.koin-project.com",
             "dnsseed.weminemnc.com")
    port = 4113
	
   
class ProCoinTestNet(ProCoin):
    """
    Class with all the necessary ProCoin testing network information based on
    https://github.com/Procoin-project/Procoin-Done/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-procoin'
    seeds = ("testnet-seed.procointools.com",
             "testnet-seed.weminemnc.com")
    port = 51474              
	
	
	