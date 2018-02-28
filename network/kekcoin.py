from clove.network.bitcoin import Bitcoin


class KekCoin(Bitcoin):
    """
    Class with all the necessary KekCoin network information based on
    https://github.com/Kekcoin-Core/kekcoin-segwit/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'kekcoin'
    symbols = ('KEK', )
    seeds = ("107.191.48.186",
             "209.250.246.178",
             "209.250.246.85")
    port = 13337


class KekCoinTestNet(KekCoin):
    """
    Class with all the necessary KekCoin testing network information based on
    https://github.com/Kekcoin-Core/kekcoin-segwit/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-kekcoin'
    seeds = ("209.250.246.85")
    port = 13777
