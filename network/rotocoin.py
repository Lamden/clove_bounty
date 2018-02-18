from clove.network.bitcoin import Bitcoin


class RotoCoin(Bitcoin):
    """
    Class with all the necessary RotoCoin network information based on
    https://github.com/rotocoin/rotocoin/blob/roto-thegreat-win/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'rotocoin'
    symbols = ('RT2', )
    seeds = ("embi.zapto.org",
             "rt2.poolerino.com",
             "91.126.200.76",
             "81.202.207.165",
             "193.242.149.63",
             "75.80.57.254",
             "188.122.8.155",
             "119.125.74.66",
             "79.136.49.122",
             "2.138.254.61")
    port = 17771
	
