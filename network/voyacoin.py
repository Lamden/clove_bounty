
from clove.network.bitcoin import Bitcoin


class Voyacoin(Bitcoin):
    """
    Class with all the necessary VOYA network information based on
    http://www.github.com/Voyacoin/Voyacoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'voyacoin'
    symbols = ('VOYA', )
    seeds = ('104.43.195.20',)
    port = 12121


class VoyacoinTestNet(Voyacoin):
    """
    Class with all the necessary VOYA testing network information based on
    http://www.github.com/Voyacoin/Voyacoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-voyacoin'
    seeds = ('104.43.195.20',)
    port = 22121
