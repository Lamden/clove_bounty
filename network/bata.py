
from clove.network.bitcoin import Bitcoin


class Bata(Bitcoin):
    """
    Class with all the necessary BTA network information based on
    http://www.github.com/BTA-BATA/BATA-SOURCE/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'bata'
    symbols = ('BTA', )
    seeds = ('list.batadnsseed.bata.io', 'batadnsseed.midnightminer.net')
    port = 5784


class BataTestNet(Bata):
    """
    Class with all the necessary BTA testing network information based on
    http://www.github.com/BTA-BATA/BATA-SOURCE/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-bata'
    seeds = ('testnet-seed.bata.io', 'testnet-bata.midnightminer.net',
             'dnsseed.wemine-testnet.com')
    port = 33813
