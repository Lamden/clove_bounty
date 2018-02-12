
from clove.network.bitcoin import Bitcoin


class Flaxscript(Bitcoin):
    """
    Class with all the necessary FLAX network information based on
    http://www.github.com/thegreatoldone/flaxscript/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'flaxscript'
    symbols = ('FLAX', )
    seeds = ('192.99.37.133', '84.200.4.67', '213.32.98.226')
    port = 17235


class FlaxscriptTestNet(Flaxscript):
    """
    Class with all the necessary FLAX testing network information based on
    http://www.github.com/thegreatoldone/flaxscript/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-flaxscript'
    seeds = ('',)
    port = 23990
