
from clove.network.bitcoin import Bitcoin


class Pandacoin(Bitcoin):
    """
    Class with all the necessary PND network information based on
    http://www.github.com/DigitalPandacoin/pandacoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'pandacoin'
    symbols = ('PND', )
    seeds = ('server1.cryptodepot.org',)
    port = 22445


class PandacoinTestNet(Pandacoin):
    """
    Class with all the necessary PND testing network information based on
    http://www.github.com/DigitalPandacoin/pandacoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-pandacoin'
    seeds = ('pndstats.com',)
    port = 44656
