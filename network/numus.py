
from clove.network.bitcoin import Bitcoin


class Numus(Bitcoin):
    """
    Class with all the necessary NMS network information based on
    http://www.github.com/numuscrypto/numuscore/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'numus'
    symbols = ('NMS', )
    seeds = ('141.255.161.78', '143.202.154.31')
    port = 28121


class NumusTestNet(Numus):
    """
    Class with all the necessary NMS testing network information based on
    http://www.github.com/numuscrypto/numuscore/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-numus'
    seeds = ()
    port = 27121
