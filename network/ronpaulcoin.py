from clove.network.bitcoin import Bitcoin


class RonPaulCoin(Bitcoin):
    """
    Class with all the necessary RonPaulCoin network information based on
    https://github.com/ronpaulcoin/ronpaulcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'ronpaulcoin'
    symbols = ('RPC', )
    seeds = ("dnsseed.ronpaulcoin.nl")
    port = 9027


class RonPaulCoinTestNet(RonPaulCoin):
    """
    Class with all the necessary RonPaulCoin testing network information based on
    https://github.com/ronpaulcoin/ronpaulcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-ronpaulcoin'
    seeds = ("testnet-seed.ronpaulcoin.nl")
    port = 19027
