from clove.network.bitcoin import Bitcoin


class FujiCoin(Bitcoin):
    """
    Class with all the necessary FJC network information based on
    https://github.com/fujicoin/fujicoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'fujicoin'
    symbols = ('FJC', )
    seeds = ()
    port = 3777


class FujiCoinTestNet(FujiCoin):
    """
    Class with all the necessary FJC testing network information based on
    https://github.com/fujicoin/fujicoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-fujicoin'
    seeds = ()
    port = 13777