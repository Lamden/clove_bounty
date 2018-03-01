from clove.network.bitcoin import Bitcoin


class DollarCoin(Bitcoin):
    """
    Class with all the necessary DLC network information based on
    https://github.com/dollarcoins/source/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'dollarcoin'
    symbols = ('DLC', )
    seeds = ()
    port = 8145


class DollarCoinTestNet(DollarCoin):
    """
    Class with all the necessary DLC testing network information based on
    https://github.com/dollarcoins/source/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-dollarcoin'
    seeds = ()
    port = 18145
