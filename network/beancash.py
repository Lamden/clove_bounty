
from clove.network.bitcoin import Bitcoin


class BeanCash(Bitcoin):
    """
    Class with all the necessary BITB network information based on
    http://www.github.com/TeamBitBean/bitbean-core/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'beancash'
    symbols = ('BITB', )
    seeds = ('stalk1.bitbean.org', 'stalk2.bitbean.org', 'stalk3.bitbean.org',
             'stalk1.beancash.net', 'stalk2.beancash.net', 'stalk3.beancash.net')
    port = 22460


class BeanCashTestNet(BeanCash):
    """
    Class with all the necessary BITB testing network information based on
    http://www.github.com/TeamBitBean/bitbean-core/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-beancash'
    seeds = ()
    port = 25714
