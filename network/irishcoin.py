
from clove.network.bitcoin import Bitcoin


class IrishCoin(Bitcoin):
    """
    Class with all the necessary IRL network information based on
    http://www.github.com/IrishCoinProject/IrishCoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'irishcoin'
    symbols = ('IRL', )
    seeds = ('node.irishcoin.org', 'dns.irishcoin.org')
    port = 12375


class IrishCoinTestNet(IrishCoin):
    """
    Class with all the necessary IRL testing network information based on
    http://www.github.com/IrishCoinProject/IrishCoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-irishcoin'
    seeds = ('testnode.irishcoin.org', 'testdns.irishcoin.org')
    port = 11375
