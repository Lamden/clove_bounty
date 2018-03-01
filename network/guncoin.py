from clove.network.bitcoin import Bitcoin


class Guncoin(Bitcoin):
    """
    Class with all the necessary Guncoin network information based on
    https://github.com/guncoin/guncoin/blob/master-1.4/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'guncoin'
    symbols = ('GUN', )
    seeds = ("seed.guncoin.info", "seed2.guncoin.info")
    port = 42954


class GuncoinTestNet(Guncoin):
    """
    Class with all the necessary Guncoin testing network information based on
    https://github.com/guncoin/guncoin/blob/master-1.4/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-guncoin'
    seeds = ("testnet-seed.guncoin.info", "testnet-seed2.guncoin.info")
    port = 52954
