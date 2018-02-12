
from clove.network.bitcoin import Bitcoin


class Adzcoin(Bitcoin):
    """
    Class with all the necessary ADZ network information based on
    http://www.github.com/AdzCoin/adzcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'adzcoin'
    symbols = ('ADZ', )
    seeds = ('seed1.cryptolife.net', 'seed2.cryptolife.net')
    port = 43029


class AdzcoinTestNet(Adzcoin):
    """
    Class with all the necessary ADZ testing network information based on
    http://www.github.com/AdzCoin/adzcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-adzcoin'
    seeds = ()
    port = 143029
