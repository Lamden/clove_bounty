from clove.network.bitcoin import Bitcoin


class HitCoin(Bitcoin):
    """
    Class with all the necessary HitCoin network information based on
    https://github.com/tradopia/HitCoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'hitcoin'
    symbols = ('HTC', )
    seeds = ("107.170.204.131",
             "107.170.126.142")
    port = 42030
