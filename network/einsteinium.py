from clove.network.bitcoin import Bitcoin


class Einsteinium(Bitcoin):
    """
    Class with all the necessary Einsteinium network information based on
    https://github.com/einsteinium/einsteinium/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'einsteinium'
    symbols = ('EMC2', )
    seeds =  ("dnsseed.einsteinium.org")
    port = 41878
	
   
class EinsteiniumTestNet(Einsteinium):
    """
    Class with all the necessary Einsteinium testing network information based on
    https://github.com/einsteinium/einsteinium/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-einsteinium'
    seeds = ("testnet-seed.einsteiniumtools.com","testnet-seed.weminemnc.com")
    port = 31878              