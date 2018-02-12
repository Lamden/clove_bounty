
from clove.network.bitcoin import Bitcoin


class i0coin(Bitcoin):
    """
    Class with all the necessary I0C network information based on
    http://www.github.com/domob1812/i0coin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'i0coin'
    symbols = ('I0C', )
    seeds = ('seed.i0coin.domob.eu',)
    port = 7333


class i0coinTestNet(i0coin):
    """
    Class with all the necessary I0C testing network information based on
    http://www.github.com/domob1812/i0coin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-i0coin'
    seeds = ()
    port = 17333
