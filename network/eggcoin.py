from clove.network.bitcoin import Bitcoin


class EggCoin(Bitcoin):
    """
    Class with all the necessary EGG network information based on
    https://github.com/eastercoindev/eggcoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'eggcoin'
    symbols = ('EGG', )
    seeds = ()
    port = 31104


class EggCoinTestNet(EggCoin):
    """
    Class with all the necessary EGG testing network information based on
    https://github.com/eastercoindev/eggcoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-eggcoin'
    seeds = ()
    port = 20134
