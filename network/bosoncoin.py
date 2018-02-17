from clove.network.bitcoin import Bitcoin


class BosonCoin(Bitcoin):
    """
    Class with all the necessary BosonCoin network information based on
    https://github.com/bosonproject/Boson/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bosoncoin'
    symbols = ('BOSON', )
    seeds = ("45.42.189.74",
             "107.190.164.220")
    port = 12090
	
   
