
from clove.network.bitcoin import Bitcoin


class SHACoin(Bitcoin):
    """
    Class with all the necessary SHA network information based on
    https://github.com/antibitcoin/antibitcoin-source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'shacoin'
    symbols = ('SHA', )
    seeds = ('seed1.shacoin.us', 'seed2.shacoin.us', 'seed3.shacoin.us')
    port = 25555


class SHACoinTestNet(SHACoin):
    """
    Class with all the necessary SHA testing network information based on
    https://github.com/antibitcoin/antibitcoin-source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-shacoin'
    seeds = ()
    port = 26555
