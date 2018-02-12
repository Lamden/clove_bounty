
from clove.network.bitcoin import Bitcoin


class OsmiumCoin(Bitcoin):
    """
    Class with all the necessary OS76 network information based on
    http://www.github.com/OS76/OSMIUMCOIN_OS76/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'osmiumcoin'
    symbols = ('OS76', )
    seeds = ('195.34.100.2',)
    port = 4947


class OsmiumCoinTestNet(OsmiumCoin):
    """
    Class with all the necessary OS76 testing network information based on
    http://www.github.com/OS76/OSMIUMCOIN_OS76/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-osmiumcoin'
    seeds = ()
    port = 14947
