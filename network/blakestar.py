from clove.network.bitcoin import Bitcoin


class BlakeStar(Bitcoin):
    """
    Class with all the necessary BlakeStar network information based on
    https://github.com/Blakestarcoin/BLASS/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'blakestar'
    symbols = ('BLAS', )
    seeds =  ("213.169.33.11")
    port = 14442
	
   
class BlakeStarTestNet(BlakeStar):
    """
    Class with all the necessary BlakeStar testing network information based on
    https://github.com/Blakestarcoin/BLASS/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-blakestar'
    seeds = ("test1.BlakeStar.pw")
    port = 24442              