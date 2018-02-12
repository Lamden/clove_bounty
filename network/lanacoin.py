
from clove.network.bitcoin import Bitcoin


class LanaCoin(Bitcoin):
    """
    Class with all the necessary LANA network information based on
    http://www.github.com/LanaCoin/lanacoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'lanacoin'
    symbols = ('LANA', )
    seeds = ('seed1.lanacoin.com', 'seed2.lanacoin.com', 'seed3.lanacoin.com', 'seed4.lanacoin.com', 'seed5.lanacoin.com', 'seed6.lanacoin.com', 'seed7.lanacoin.com', 'seed8.lanacoin.com', 'seed9.lanacoin.com')
    port = 7506


class LanaCoinTestNet(LanaCoin):
    """
    Class with all the necessary LANA testing network information based on
    http://www.github.com/LanaCoin/lanacoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-lanacoin'
    seeds = ('test1.lanacoin.com', 'test2.lanacoin.com')
    port = 17506
