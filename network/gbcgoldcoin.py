from clove.network.bitcoin import Bitcoin


class GBCGoldCoin(Bitcoin):
    """
    Class with all the necessary GBCGoldCoin network information based on
    https://github.com/jpgagnon/qbc/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'gbcgoldcoin'
    symbols = ('GBC', )
    seeds = ("dnsseed.qbc.io", "54.86.39.92")
    port = 56790


class GBCGoldCoinTestNet(GBCGoldCoin):
    """
    Class with all the necessary GBCGoldCoin testing network information based on
    https://github.com/jpgagnon/qbc/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-gbcgoldcoin'
    seeds = ("testnet-seed.qbc.io")
    port = 46790
