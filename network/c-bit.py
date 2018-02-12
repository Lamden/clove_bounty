
from clove.network.bitcoin import Bitcoin


class C-Bit(Bitcoin):
    """
    Class with all the necessary XCT network information based on
    http://www.github.com/Infernoman/C-Bit/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'c-bit'
    symbols = ('XCT', )
    seeds = ('192.241.191.47',)
    port = 8289


class C-BitTestNet(C-Bit):
    """
    Class with all the necessary XCT testing network information based on
    http://www.github.com/Infernoman/C-Bit/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-c-bit'
    seeds = ('159.203.31.151', '192.241.179.42')
    port = 18289
