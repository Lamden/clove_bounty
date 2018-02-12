
from clove.network.bitcoin import Bitcoin


class Sharkcoin(Bitcoin):
    """
    Class with all the necessary SAK network information based on
    http://www.github.com/shark-git/sharkcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'sharkcoin'
    symbols = ('SAK', )
    seeds = ('seed1.sak.cc', 'seed2.sak.cc')
    port = 4011


class SharkcoinTestNet(Sharkcoin):
    """
    Class with all the necessary SAK testing network information based on
    http://www.github.com/shark-git/sharkcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-sharkcoin'
    seeds = ()
    port = 14011
