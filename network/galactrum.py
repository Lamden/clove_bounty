from clove.network.bitcoin import Bitcoin


class Galactrum(Bitcoin):
    """
    Class with all the necessary Galactrum network information based on
    https://github.com/galactrum/galactrum/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'galactrum'
    symbols = ('ORE', )
    seeds = ("seed1.galactrum.network",
             "seed2.galactrum.network",
             "seed3.galactrum.network",
             "seed4.galactrum.network",
             "seed5.galactrum.network")
    port = 6270
	
   
class GalactrumTestNet(Galactrum):
    """
    Class with all the necessary Galactrum testing network information based on
    https://github.com/galactrum/galactrum/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-galactrum'
    seeds = ("seed1.testnet.galactrum.network")
    port = 16270              
	
