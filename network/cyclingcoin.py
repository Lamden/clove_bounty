from clove.network.bitcoin import Bitcoin


class CyclingCoin(Bitcoin):
    """
    Class with all the necessary CYC network information based on
    https://github.com/cyclingcoin/cyclingcoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'cyclingcoin'
    symbols = ('CYC', )
    seeds = ()
    port = 15394


class CyclingCoinTestNet(CyclingCoin):
    """
    Class with all the necessary CYC testing network information based on
    https://github.com/cyclingcoin/cyclingcoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-cyclingcoin'
    seeds = ()
    port = 15494
