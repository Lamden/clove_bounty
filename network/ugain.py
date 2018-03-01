
from clove.network.bitcoin import Bitcoin


class Ugain(Bitcoin):
    """
    Class with all the necessary GAIN network information based on
    https://github.com/ugain1/ugain-src/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'ugain'
    symbols = ('GAIN', )
    seeds = ()
    port = 7891


class UgainTestNet(Ugain):
    """
    Class with all the necessary GAIN testing network information based on
    https://github.com/ugain1/ugain-src/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-ugain'
    seeds = ()
    port = 17891
