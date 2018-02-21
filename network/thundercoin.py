from clove.network.bitcoin import Bitcoin


class Thundercoin(Bitcoin):
    """
    Class with all the necessary Thundercoin network information based on
    https://github.com/VanIerselDev/Thundercoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'thundercoin'
    symbols = ('TUC', )
    seeds = ("dnsseed.litecointools.com",
             "dnsseed.litecoinpool.org",
             "dnsseed.ltc.xurious.com",
             "dnsseed.koin-project.com",
             "dnsseed.weminemnc.com")
    port = 94383
	
   
class ThundercoinTestNet(Thundercoin):
    """
    Class with all the necessary Thundercoin testing network information based on
    https://github.com/VanIerselDev/Thundercoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'test-thundercoin'
    seeds = ("testnet-seed.litecointools.com",
             "testnet-seed.ltc.xurious.com",
             "dnsseed.wemine-testnet.com")
    port = 64547               
	
	
	
	
	
