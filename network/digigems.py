from clove.network.bitcoin import Bitcoin


class Digigems(Bitcoin):
    """
    Class with all the necessary Digigems network information based on
    https://github.com/jarno83/digigems/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'digigems'
    symbols = ('DGMS', )
    seeds = ("54.69.225.67")
    port = 5333


class DigigemsTestNet(Digigems):
    """
    Class with all the necessary Digigems testing network information based on
    https://github.com/jarno83/digigems/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-digigems'
    seeds = ("88.196.13.22")
    port = 15333
