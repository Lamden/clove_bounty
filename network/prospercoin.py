from clove.network.bitcoin import Bitcoin


class ProsperCoin(Bitcoin):
    """
    Class with all the necessary ProsperCoin network information based on
    https://github.com/ProsperCoin/prospercoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'prospercoin'
    symbols = ('PRC', )
    seeds = ("seed.inmean.com",
             "seed.khmer.biz")
    port = 9431
	
   
class ProsperCoinTestNet(ProsperCoin):
    """
    Class with all the necessary ProsperCoin testing network information based on
    https://github.com/ProsperCoin/prospercoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-prospercoin'
    seeds = ("seedtest.inmean.com",
             "seed2.khmer.biz")
    port = 19222              
	
