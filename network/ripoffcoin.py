from clove.network.bitcoin import Bitcoin


class RipoffCoin(Bitcoin):
    """
    Class with all the necessary RipoffCoin network information based on
    https://github.com/RipoffCoin/RipoffCoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'ripoffcoin'
    symbols = ('RIPO', )
    seeds = ("seed.ripoffcoin.com")
    port = 54001
	
   
class RipoffCoinTestNet(Diamond):
    """
    Class with all the necessary RipoffCoin testing network information based on
    https://github.com/RipoffCoin/RipoffCoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-ripoffcoin'
    seeds = ("seedtest.ripoffcoin.com")
    port = 54002               