from clove.network.bitcoin import Bitcoin


class Mincoin(Bitcoin):
    """
    Class with all the necessary Mincoin network information based on
    https://github.com/mincoin/mincoin/blob/0.8/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'mincoin'
    symbols = ('MNC', )
    seeds = ("seed.mincointools.com",
	         "seed.mincoinpool.org")
    port = 9334
	
   
class MincoinTestNet(Mincoin):
    """
    Class with all the necessary Mincoin testing network information based on
    https://github.com/mincoin/mincoin/blob/0.8/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-mincoin'
    seeds = ("testnet-seed.mincointools.com",
	         "testnet-seed.mincoinpool.org")
    port = 19334               