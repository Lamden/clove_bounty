
from clove.network.bitcoin import Bitcoin


class SecureCoin(Bitcoin):
    """
    Class with all the necessary SRC network information based on
    http://www.github.com/securecoin/Securecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'securecoin'
    symbols = ('SRC', )
    seeds = ('securecoin.org',)
    port = 12567


class SecureCoinTestNet(SecureCoin):
    """
    Class with all the necessary SRC testing network information based on
    http://www.github.com/securecoin/Securecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-securecoin'
    seeds = ()
    port = 22567
