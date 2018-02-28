from clove.network.bitcoin import Bitcoin


class SpreadCoin(Bitcoin):
    """
    Class with all the necessary SpreadCoin network information based on
    https://github.com/spreadcoin/spreadcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'spreadcoin'
    symbols = ('SPR', )
    seeds = ("dnsseed.spreadcoin.net")
    port = 41678


class SpreadCoinTestNet(SpreadCoin):
    """
    Class with all the necessary SpreadCoin testing network information based on
    https://github.com/spreadcoin/spreadcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-spreadcoin'
    seeds = ("testnet-seed.darkcoin.io", "testnet-seed.darkcoin.qa")
    port = 51678
