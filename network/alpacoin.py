from clove.network.bitcoin import Bitcoin


class AlpaCoin(Bitcoin):
    """
    Class with all the necessary AlpaCoin network information based on
    https://github.com/maxsnowzz/Alpacoin/blob/master/Alpacoin-qt/alpacoin-source/src/chainparams.cpp
    (date of access: 02/13/2018)
    """
    name = 'alpacoin'
    symbols = ('APC', )
    seeds = ("seed1.cryptolife.net",
             "seed2.cryptolife.net",
             "explore.cryptolife.net",
             "wallet.cryptolife.net")
    port = 12873


class AlpaCoinTestNet(AlpaCoin):
    """
    Class with all the necessary AlpaCoin testing network information based on
    https://github.com/maxsnowzz/Alpacoin/blob/master/Alpacoin-qt/alpacoin-source/src/chainparams.cpp
    (date of access: 02/13/2018)
    """
    name = 'test-alpacoin'
    seeds = ("test.AlpaCoin.org", )
    port = 11835
