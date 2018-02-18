from clove.network.bitcoin import Bitcoin


class Woodcoin(Bitcoin):
    """
    Class with all the necessary Woodcoin (LOG) network information based on
    https://github.com/funkshelper/woodcore/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'woodcoin'
    symbols = ('LOG', )
    seeds = ('dnsseed.woodcoin.org')
    port = 8338


class WoodcoinTestNet(Woodcoin):
    """
    Class with all the necessary Woodcoin (LOG) testing network information based on
    https://github.com/funkshelper/woodcore/blob/master/src/chainparams.cpp    
    (date of access: 02/17/2018)
    """
    name = 'test-woodcoin'
    seeds = ('dnsseed.woodcointools.com')
    port = 18338
