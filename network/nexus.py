from clove.network.bitcoin import Bitcoin


class Nexus(Bitcoin):
    """
    Class with all the necessary Nexus NXS network information based on
    https://github.com/Nexusoft/Nexus/blob/master/src/net/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'nexus'
    symbols = ('NXS', )
    seeds = ('204.27.62.234')
    port = 9323


class NexusTestNet(Nexus):
    """
    Class with all the necessary Nexus NXS testing network information based on
    https://github.com/Nexusoft/Nexus/blob/master/src/net/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-nexus'
    seeds = ()
    port = 8313
