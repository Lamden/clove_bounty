from clove.network.bitcoin import Bitcoin


class Navcoin(Bitcoin):
    """
    Class with all the necessary NAV Coin (NAV) network information based on
    https://github.com/NAVCoin/navcoin-core/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'navcoin'
    symbols = ('NAV', )
    nodes = ('95.183.51.56', '95.183.52.55', '95.183.52.28',
             '95.183.52.29', '95.183.53.184')
    port = 44440


class NavcoinTestNet(Navcoin):
    """
    Class with all the necessary  NAV Coin (NAV) testing network information based on
    https://github.com/NAVCoin/navcoin-core/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-navcoin'
    seeds = ()
    port = 15556
