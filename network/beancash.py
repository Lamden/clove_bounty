
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
    message_start = b'\xa4\xd2\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 3,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 131
    }


class BeanCashTestNet(BeanCash):
    """
    Class with all the necessary BITB testing network information based on
    http://www.github.com/TeamBitBean/bitbean-core/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-beancash'
    seeds = ()
    port = 25714
    message_start = b'\xad\xf1\xc2\xaf'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
