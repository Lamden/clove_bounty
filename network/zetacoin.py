from clove.network.bitcoin import Bitcoin


class Zetacoin(Bitcoin):
    """
    Class with all the necessary ZET network information based on
    http://www.github.com/zetacoin/zetacoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'zetacoin'
    symbols = ('ZET', )
    seeds = (
        'seed1.zetac.org', 'seed2.zetac.org', 'seed3.zetac.org', 'seed4.zetac.org', 'seed5.zetac.org',
        'seed6.zetac.org', 'seed7.zetac.org', 'seed8.zetac.org', 'zeta1.twilightparadox.com',
        'zeta2.twilightparadox.com', 'zeta3.twilightparadox.com', 'zeta4.twilightparadox.com'
    )
    port = 17333


class ZetacoinTestNet(Zetacoin):
    """
    Class with all the necessary ZET testing network information based on
    http://www.github.com/zetacoin/zetacoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-zetacoin'
    seeds = ('test1.zetatestnet.pw',
             'test2.zetatestnet.pw', 'test3.zetatestnet.pw')
    port = 27333
