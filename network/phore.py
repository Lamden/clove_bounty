
from clove.network.bitcoin import Bitcoin


class Phore(Bitcoin):
    """
    Class with all the necessary PHR network information based on
    http://www.github.com/phoreproject/Phore/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'phore'
    symbols = ('PHR', )
    seeds = ('dns0.phore.io', 'dns1.phore.io', 'dns2.phore.io', 'dns3.phore.io', 'dns4.phore.io',
             'dns5.phore.io', 'dns6.phore.io', 'dns7.phore.io', 'dns8.phore.io', 'dns9.phore.io')
    port = 11771


class PhoreTestNet(Phore):
    """
    Class with all the necessary PHR testing network information based on
    http://www.github.com/phoreproject/Phore/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-phore'
    seeds = ()
    port = 11773
