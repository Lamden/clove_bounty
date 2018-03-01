from clove.network.bitcoin import Bitcoin


class TotCoin(Bitcoin):
    """
    Class with all the necessary TotCoin network information based on
    https://github.com/totcoindev/totcoin/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'totcoin'
    symbols = ('TOT', )
    seeds = ("78.113.252.129")
    port = 42400


class TotCoinTestNet(TotCoin):
    """
    Class with all the necessary TotCoin testing network information based on
    https://github.com/totcoindev/totcoin/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-totcoin'
    seeds = ("soscoindev.ddns.net")
    port = 19999
