
from clove.network.bitcoin import Bitcoin


class PlatinumBAR(Bitcoin):
    """
    Class with all the necessary XPTX network information based on
    http://www.github.com/xptx/PlatinumBar/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'platinumbar'
    symbols = ('XPTX', )
    seeds = ('159.203.21.62', 'seed1.platinumbar.io', 'seed2.platinumbar.io',
             'seed3.platinumbar.io', 'seed4.platinumbar.io', 'seed5.platinumbar.io')
    port = 18993


class PlatinumBARTestNet(PlatinumBAR):
    """
    Class with all the necessary XPTX testing network information based on
    http://www.github.com/xptx/PlatinumBar/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-platinumbar'
    seeds = ()
    port = 15001
