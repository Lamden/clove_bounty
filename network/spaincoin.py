from clove.network.bitcoin import Bitcoin


class Spaincoin(Bitcoin):
    """
    Class with all the necessary Spaincoin network information based on
    https://github.com/SpainCoinProject/spaincoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'spaincoin'
    symbols = ('DMD', )
    seeds = ("dnsseed.ds.spaincoin.org",
             "dnsseed.spaincoin.org")
    port = 11492
	
   
class SpaincoinTestNet(Spaincoin):
    """
    Class with all the necessary Spaincoin testing network information based on
    https://github.com/SpainCoinProject/spaincoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-spaincoin'
    seeds = ("dnsseed.spaincoin.org")
    port = 21492              
	
