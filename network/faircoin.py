from clove.network.bitcoin import Bitcoin


class FairCoin(Bitcoin):
    """
    Class with all the necessary FairCoin network information based on
    https://github.com/faircoin/faircoin/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'faircoin'
    symbols = ('FAIR', )
    seeds = ("faircoin2-seed1.fair-coin.org",
             "faircoin2-seed2.fair-coin.org")
    port = 40404


class FairCoinTestNet(FairCoin):
    """
    Class with all the necessary FairCoin testing network information based on
    https://github.com/faircoin/faircoin/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-faircoin'
    seeds = ("faircoin2-testnet-seed1.fair-coin.org")
    port = 41404
