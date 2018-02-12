from clove.network.bitcoin import Bitcoin


class Peercoin(Bitcoin):
    """
    Class with all the necessary Peercoin (PPC) network information based on
    https://github.com/peercoin/peercoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'peercoin'
    symbols = ('PPC', )
    seeds = ('seed.peercoin.net', 'seed.ppcoin.net')
    port = 9901


class Peercoin(Peercoin):
    """
    Class with all the necessary Peercoin (PPC) testing network information based on
    https://github.com/peercoin/peercoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-peercoin'
    seeds = ('tseed.peercoin.net')
    port = 9903
