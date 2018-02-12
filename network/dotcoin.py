
from clove.network.bitcoin import Bitcoin


class Dotcoin(Bitcoin):
    """
    Class with all the necessary DOT network information based on
    http://www.github.com/CryptopiaNZ/DOT/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'dotcoin'
    symbols = ('DOT', )
    seeds = ('162.255.117.105', 'nodes1.cryptopia.co.nz', 'nodes2.cryptopia.co.nz', 'pools1.cryptopia.co.nz', 'pools2.cryptopia.co.nz')
    port = 19745


class DotcoinTestNet(Dotcoin):
    """
    Class with all the necessary DOT testing network information based on
    http://www.github.com/CryptopiaNZ/DOT/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-dotcoin'
    seeds = ('dot.testseeds.triplehexxx.net',)
    port = 119745
