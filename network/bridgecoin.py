from clove.network.bitcoin import Bitcoin


class BridgeCoin(Bitcoin):
    """
    Class with all the necessary BridgeCoin network information based on
    https://github.com/CryptoBridge/bridgecoin/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'bridgecoin'
    symbols = ('BCO', )
    seeds = ("seed1.bridgecoin.org",
             "seed2.bridgecoin.org",
             "seed3.bridgecoin.org")
    port = 6333
	
   
class BridgeCoinTestNet(BridgeCoin):
    """
    Class with all the necessary BridgeCoin testing network information based on
    https://github.com/CryptoBridge/bridgecoin/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-bridgecoin'
    seeds = ("seed1.bridgecoin.org",
             "seed2.bridgecoin.org",
             "seed3.bridgecoin.org")
    port = 16333              
	
