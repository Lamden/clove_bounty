from clove.network.bitcoin import Bitcoin


class KZCash(Bitcoin):
    """
    Class with all the necessary KZCash (KZC) network information based on
    https://github.com/kzcashteam/kzcash/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'kzcash'
    symbols = ('KZC', )
    seeds = ('dnsseed.kzcash.kz', )
    port = 8277


class KZCashTestNet(KZCash):
    """
    Class with all the necessary KZCash (KZC) testing network information based on
    https://github.com/kzcashteam/kzcash/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-kzcash'
    seeds = ('testdnsseed.kzcash.kz', )
    port = 18277
