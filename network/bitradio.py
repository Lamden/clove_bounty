
from clove.network.bitcoin import Bitcoin


class Bitradio(Bitcoin):
    """
    Class with all the necessary BRO network information based on
    http://www.github.com/thebitradio/Bitradio/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'bitradio'
    symbols = ('BRO', )
    seeds = ('node1.bitrad.io', 'node2.bitrad.io', 'node3.bitrad.io')
    port = 32454


class BitradioTestNet(Bitradio):
    """
    Class with all the necessary BRO testing network information based on
    http://www.github.com/thebitradio/Bitradio/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-bitradio'
    seeds = ()
    port = 58870
