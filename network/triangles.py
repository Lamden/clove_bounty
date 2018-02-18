from clove.network.bitcoin import Bitcoin


class Triangles(Bitcoin):
    """
    Class with all the necessary Triangles network information based on
    https://github.com/TrianglesProject/triangles/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'triangles'
    symbols = ('TRI', )
    seeds = ("dnsseed.bit.diamonds")
    port = 17771
	
   
class DiamondTestNet(Diamond):
    """
    Class with all the necessary Diamond testing network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-diamond'
    seeds = ("dnsseed.bit.diamonds")
    port = 51474              