from clove.network.bitcoin import Bitcoin


class TopazCoin(Bitcoin):
    """
    Class with all the necessary  Topaz Coin (TOPAZ) network information based on
    https://github.com/CryptoCoderz/TOPAZ/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'topazcoin'
    symbols = ('TOPAZ', )
    seeds = ('91.134.120.210')
    port = 6909


class TopazCoinTestNet(TopazCoin):
    """
    Class with all the necessary  Topaz Coin (TOPAZ) network information based on
    https://github.com/CryptoCoderz/TOPAZ/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-topazcoin'
    symbols = ('TOPAZ', )
    seeds = ()
    port = 6808
