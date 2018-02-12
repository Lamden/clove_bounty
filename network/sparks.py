
from clove.network.bitcoin import Bitcoin


class Sparks(Bitcoin):
    """
    Class with all the necessary SPK network information based on
    https://github.com/sparkscrypto/Sparks/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'sparks'
    symbols = ('SPK', )
    seeds = (
        'seed.sparks.gold',
        'explorer.sparks.gold'
    )
    port = 8890


class SparksTestNet(Sparks):
    """
    Class with all the necessary SPK testing network information based on
    https://github.com/sparkscrypto/Sparks/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-sparks'
    seeds = ()
    port = 8891
