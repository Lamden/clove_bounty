from clove.network.bitcoin import Bitcoin


class ChampCoin(Bitcoin):
    """
    Class with all the necessary ChampCoin network information based on
    https://github.com/ChampCoin/Champ/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'champcoin'
    symbols = ('TCC', )
    seeds = ("champcointools.com")
    port = 38173
	
   
class ChampCoinTestNet(ChampCoin):
    """
    Class with all the necessary ChampCoin testing network information based on
    https://github.com/ChampCoin/Champ/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'test-champcoin'
    seeds = ("testnet-seed.champcointools.com",
             "testnet-seed.champ.xurious.com",
             "dnsseed.wemine-testnet.com")	
    port = 39173               
	
