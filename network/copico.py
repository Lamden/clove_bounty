
from clove.network.bitcoin import Bitcoin


class Copico(Bitcoin):
    """
    Class with all the necessary XCPO network information based on
    http://www.github.com/copicogithub1/copico/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'copico'
    symbols = ('XCPO', )
    seeds = ('seed1.copico.io', 'seed2.copico.io')
    port = 17356


class CopicoTestNet(Copico):
    """
    Class with all the necessary XCPO testing network information based on
    http://www.github.com/copicogithub1/copico/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-copico'
    seeds = ()
    port = 17357
