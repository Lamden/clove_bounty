from clove.network.bitcoin import Bitcoin


class HTMLCOIN(Bitcoin):
    """
    Class with all the necessary HTMLCOIN network information based on
    https://github.com/HTMLCOIN/HTMLCOIN/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'htmlcoin'
    symbols = ('HTML', )
    seeds = ("seed1.htmlcoin.com",
             "seed2.htmlcoin.com",
             "seed3.htmlcoin.com",
             "seed4.htmlcoin.com")
    port = 4888
	
   
class HTMLCOINTestNet(HTMLCOIN):
    """
    Class with all the necessary HTMLCOIN testing network information based on
    https://github.com/HTMLCOIN/HTMLCOIN/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-htmlcoin'
    seeds = ("testnet-seed1.htmlcoin.com","testnet-seed2.htmlcoin.com")
    port = 14888              
	
