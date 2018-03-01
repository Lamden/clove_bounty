
from clove.network.bitcoin import Bitcoin


class Zeitcoin(Bitcoin):
    """
    Class with all the necessary ZEIT network information based on
    https://github.com/zeitcoin/zeitcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'zeitcoin'
    symbols = ('ZEIT', )
    seeds = ('seed.zeit-coin.net', 'zeitseed2.ddns.net', 'seed.aeternity.cc')
    port = 44845


class ZeitcoinTestNet(Zeitcoin):
    """
    Class with all the necessary ZEIT testing network information based on
    https://github.com/zeitcoin/zeitcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-zeitcoin'
    seeds = ()
    port = 22788
