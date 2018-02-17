from clove.network.bitcoin import Bitcoin


class Fractalcoin(Bitcoin):
    """
    Class with all the necessary Fractalcoin network information based on
    https://github.com/fractalcoin/fractalcoin/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'fractalcoin'
    symbols = ('FRAC', )
    seeds = ("seed1.fractalcoin.net",
             "seed2.fractalcoin.net",
             "seed3.fractalcoin.net",
             "seed4.fractalcoin.net",
             "seed5.fractalcoin.net",
             "seed6.fractalcoin.net",
             "seed7.fractalcoin.net",
             "seed8.fractalcoin.net",
             "seed1.fractalco.in",
             "seed2.fractalco.in",
             "seed3.fractalco.in",
             "seed4.fractalco.in",
             "seed5.fractalco.in",
             "seed6.fractalco.in",
             "seed7.fractalco.in",
             "seed8.fractalco.in",
             "earlz.net")
    port = 33112
	
   
class FractalcoinTestNet(Fractalcoin):
    """
    Class with all the necessary Fractalcoin testing network information based on
    https://github.com/fractalcoin/fractalcoin/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-fractalcoin'
    seeds = ("testnet.fractalcoin.net",
             "earlz.net",
             "seed1.fractalcoin.net",
             "seed2.fractalcoin.net",
             "seed3.fractalcoin.net",
             "seed4.fractalcoin.net",
             "seed5.fractalcoin.net",
             "seed6.fractalcoin.net",
             "seed7.fractalcoin.net",
             "seed8.fractalcoin.net",
             "seed1.fractalco.in",
             "seed2.fractalco.in",
             "seed3.fractalco.in",
             "seed4.fractalco.in",
             "seed5.fractalco.in",
             "seed6.fractalco.in",
             "seed7.fractalco.in",
             "seed8.fractalco.in")
    port = 44112              
	

