
from clove.network.bitcoin import Bitcoin


class Visio(Bitcoin):
    """
    Class with all the necessary VISIO network information based on
    http://www.github.com/Fladirmacht/visioX/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'visio'
    symbols = ('VISIO', )
    seeds = ('seed.visio.wtf', 'seeda.visio.wtf', 'seedb.visio.wtf', 'seedc.visio.wtf', '94.102.50.82', '185.145.131.149')
    port = 16778


class VisioTestNet(Visio):
    """
    Class with all the necessary VISIO testing network information based on
    http://www.github.com/Fladirmacht/visioX/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-visio'
    seeds = ()
    port = 25714
