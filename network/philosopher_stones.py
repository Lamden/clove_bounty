
from clove.network.bitcoin import Bitcoin


class PhilosopherStones(Bitcoin):
    """
    Class with all the necessary PHS network information based on
    https://github.com/vladk75/philosopherstone/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'philosopherstones'
    symbols = ('PHS', )
    seeds = ('node1.philosopherstones.org', 'node2.philosopherstones.org',
             'node3.philosopherstones.org', 'node4.philosopherstones.org')
    port = 16281


class PhilosopherStonesTestNet(PhilosopherStones):
    """
    Class with all the necessary PHS testing network information based on
    https://github.com/vladk75/philosopherstone/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-philosopherstones'
    seeds = ()
    port = 26281
