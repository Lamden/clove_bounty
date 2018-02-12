from clove.network.bitcoin import Bitcoin


class DotCoin(Bitcoin):
    """
    Class with all the necessary DotCoin network information based on
    https://github.com/cryptopianz/dot/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'dotcoin'
    symbols = ('DOT', )
    seeds =  ("162.255.117.105","nodes1.cryptopia.co.nz","nodes2.cryptopia.co.nz","pools1.cryptopia.co.nz","pools2.cryptopia.co.nz")
    port = 19745
	
	
class DotCoinTestNet(DotCoin):
    """
    Class with all the necessary DotCoin testing network information based on
    https://github.com/cryptopianz/dot/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-dotcoin'
    seeds = ()
    port = 119745            
	
	
	