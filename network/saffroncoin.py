from clove.network.bitcoin import Bitcoin


class Saffroncoin(Bitcoin):
    """
    Class with all the necessary Saffroncoin network information based on
    https://github.com/saffroncoin/saffroncoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'saffroncoin'
    symbols = ('SFR', )
    seeds = ("saffroncoin.com",
             "182.18.175.110")
    port = 19717
	
   
class SaffroncoinTestNet(Saffroncoin):
    """
    Class with all the necessary Saffroncoin testing network information based on
    https://github.com/saffroncoin/saffroncoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-saffroncoin'
    seeds = ("testseed1.saffroncoin.org")
    port = 29717              