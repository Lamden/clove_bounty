
from clove.network.bitcoin import Bitcoin


class Catcoin(Bitcoin):
    """
    Class with all the necessary CAT network information based on
    http://www.github.com/CatcoinOfficial/CatcoinRelease/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'catcoin'
    symbols = ('CAT', )
    seeds = ('seed.catcoinwallets.com', 'cat.geekhash.org')
    port = 9933


class CatcoinTestNet(Catcoin):
    """
    Class with all the necessary CAT testing network information based on
    http://www.github.com/CatcoinOfficial/CatcoinRelease/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-catcoin'
    seeds = ('seed.catcoinwallets.com',)
    port = 19933
