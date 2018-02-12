from clove.network.bitcoin import Bitcoin


class Beatscoin(Bitcoin):
    """
    Class with all the necessary Beatscoin network information based on
    https://github.com/beatscoindev/beatscoinv2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Beatscoin'
    symbols = ('XBTS', )
    seeds = ('81.4.125.138')
    port = 26152


class BeatscoinTestNet(Beatscoin):
    """
    Class with all the necessary Beatscoin testing network information based on
    https://github.com/beatscoindev/beatscoinv2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-Beatscoin'
    seeds = ()
    port = 26153 
	
	
	