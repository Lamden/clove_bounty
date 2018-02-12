from clove.network.bitcoin import Bitcoin


class IrishCoin(Bitcoin):
    """
    Class with all the necessary IrishCoin network information based on
    https://github.com/irishcoinproject/irishcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'irishcoin'
    symbols = ('IRL', )
    seeds = ('node.irishcoin.org', 'dns.irishcoin.org')
    port = 12375


classIrishCoinTestNet(IrishCoin):
    """
    Class with all the necessary IrishCoin testing network information based on
    https://github.com/irishcoinproject/irishcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-irishcoin'
    seeds = ('testnode.irishcoin.org','testdns.irishcoin.org')
    port = 11375 