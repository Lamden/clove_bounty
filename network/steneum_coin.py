
from clove.network.bitcoin import Bitcoin


class SteneumCoin(Bitcoin):
    """
    Class with all the necessary STN network information based on
    http://www.github.com/dhabitafx/steneum/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'steneum-coin'
    symbols = ('STN', )
    seeds = ('64.20.57.229',)
    port = 26965


class SteneumCoinTestNet(SteneumCoin):
    """
    Class with all the necessary STN testing network information based on
    http://www.github.com/dhabitafx/steneum/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-steneum-coin'
    seeds = ()
    port = 36965
