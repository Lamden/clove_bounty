from clove.network.bitcoin import Bitcoin


class Tomatocoin(Bitcoin):
    """
    Class with all the necessary Tomatocoin network information based on
    https://github.com/Tomatocoin/tomatocoin-master/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'tomatocoin'
    symbols = ('TMT', )
    seeds = ("23.23.186.131")
    port = 9888
	
   
class TomatocoinTestNet(Tomatocoin):
    """
    Class with all the necessary Tomatocoin testing network information based on
    https://github.com/Tomatocoin/tomatocoin-master/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'test-tomatocoin'
    seeds = ("23.23.186.131")
    port = 19888              