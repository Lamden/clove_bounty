from clove.network.bitcoin import Bitcoin


class PirateCoin(Bitcoin):
    """
    Class with all the necessary PirateCoin network information based on
    https://github.com/kebian/Piratecoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'piratecoin'
    symbols = ('PIR', )
    seeds = ("dnsseed.piratecoin.co")
    port = 17771
	
# no 11656