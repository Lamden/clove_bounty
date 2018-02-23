from clove.network.bitcoin import Bitcoin


class SambaCoin(Bitcoin):
    """
    Class with all the necessary SambaCoin network information based on
    https://github.com/sambacoin/sambacoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'sambacoin'
    symbols = ('SMB', )
    seeds = ("seed1.sambacoin.info",
             "seed2.sambacoin.info",
             "seed.sambacoin.info",
             "seed3.sambacoin.info",
             "seed4.sambacoin.info",
             "seed5.sambacoin.info",
             "seed6.sambacoin.info")
    port = 11255
	
   
class SambaCoinTestNet(SambaCoin):
    """
    Class with all the necessary SambaCoin testing network information based on
    https://github.com/sambacoin/sambacoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'test-sambacoin'
    seeds = ("seed1-testnet.sambacoin.info",
             "seed2-testnet.sambacoin.info",
             "seed-testnet.sambacoin.info")
    port = 21255              
	
	
