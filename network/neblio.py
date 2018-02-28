from clove.network.bitcoin import Bitcoin


class Neblio(Bitcoin):
    """
    Class with all the necessary Neblio (NEBL) network information based on
    https://github.com/NeblioTeam/neblio/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'neblio'
    symbols = ('NEBL', )
    seeds = ('seed.nebl.io')
    port = 6325


class NeblioTestNet(Neblio):
    """
    Class with all the necessary Neblio (NEBL) testing network information based on
    https://github.com/NeblioTeam/neblio/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-neblio'
    seeds = ()
    port = 16325
