from clove.network.bitcoin import Bitcoin


class Furrycoin(Bitcoin):
    """
    Class with all the necessary Furrycoin network information based on
    https://github.com/prolifik/Furrycoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'furrycoin'
    symbols = ('FUR', )
    seeds = ("seed1.furrycoin.net")
    port = 11000
	
   
class FurrycoinTestNet(Furrycoin):
    """
    Class with all the necessary Furrycoin testing network information based on
    https://github.com/prolifik/Furrycoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'test-furrycoin'
    seeds = ("test-seed1.furrycoin.net")
    port = 5744              