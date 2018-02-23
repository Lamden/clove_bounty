from clove.network.bitcoin import Bitcoin


class Bellscoin(Bitcoin):
    """
    Class with all the necessary Bellscoin network information based on
    https://github.com/bells-coin/bells-coin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'bellscoin'
    symbols = ('BEL', )
    seeds = ("node0.bellscoin.com",
             "dnsseed.Bellspool.org",
             "203.20.114.252",
             "31.31.202.138")
    port = 19919
	
   
class BellscoinTestNet(Bellscoin):
    """
    Class with all the necessary Bellscoin testing network information based on
    https://github.com/bells-coin/bells-coin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'test-bellscoin'
    seeds = ("testnet-seed.Bellstools.com",
             "testnet-seed.BELLS.xurious.com",
             "dnsseed.wemine-testnet.com")
    port = 29919               
	

