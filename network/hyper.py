
from clove.network.bitcoin import Bitcoin


class Hyper(Bitcoin):
    """
    Class with all the necessary HYPER network information based on
    http://www.github.com/CryptoDatabase/hyper/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'hyper'
    symbols = ('HYPER', )
    seeds = ('195.74.52.227', 'NULL')
    port = 11194


class HyperTestNet(Hyper):
    """
    Class with all the necessary HYPER testing network information based on
    http://www.github.com/CryptoDatabase/hyper/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-hyper'
    seeds = ()
    port = 11199
