from clove.network.bitcoin import Bitcoin


class Sakuracoin(Bitcoin):
    """
    Class with all the necessary Sakuracoin network information based on
    https://github.com/sakuracoin-project/sakuracoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'sakuracoin'
    symbols = ('SKR', )
    seeds = ("skrseed.sighash.info")
    port = 9301
	
   
class SakuracoinTestNet(Sakuracoin):
    """
    Class with all the necessary Sakuracoin testing network information based on
    https://github.com/sakuracoin-project/sakuracoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-sakuracoin'
    seeds = ("skrseed.sighash.info")
    port = 19301              