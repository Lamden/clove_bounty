from clove.network.bitcoin import Bitcoin


class LBRYCredits(Bitcoin):
    """
    Class with all the necessary  LBRY Credits (LBC) network information based on
    https://github.com/lbryio/lbrycrd/blob/master/src/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'lbry_credits'
    symbols = ('LBC', )
    seeds = ('dnsseed1.lbry.io', 'dnsseed2.lbry.io', 'dnsseed3.lbry.io')
    port = 9246


class LBRYCreditsTestNet(LBRYCredits):
    """
    Class with all the necessary  LBRY Credits (LBC) network information based on
    https://github.com/lbryio/lbrycrd/blob/master/src/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-lbry_credits'
    symbols = ('LBC', )
    seeds = ('testdnsseed1.lbry.io', 'testdnsseed1.lbry.io')
    port = 19246
