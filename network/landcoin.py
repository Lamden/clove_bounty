from clove.network.bitcoin import Bitcoin


class LandCoin(Bitcoin):
    """
    Class with all the necessary LandCoin network information based on
    https://github.com/landcoin-project/landcoin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'landcoin'
    symbols = ('LND', )
    seeds = ("seed.landcoin.net")
    port = 1911


class LandCoinTestNet(LandCoin):
    """
    Class with all the necessary LandCoin testing network information based on
    https://github.com/landcoin-project/landcoin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-landcoin'
    seeds = ("seed.landcoin.net")
    port = 11911
