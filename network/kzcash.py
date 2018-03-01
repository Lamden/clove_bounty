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
    message_start = b'\xbd\x1b\x44\xba'
    base58_prefixes = {
        'PUBKEY_ADDR': 46,
        'SCRIPT_ADDR': 16,
        'SECRET_KEY': 204
    }


class KZCashTestNet(KZCash):
    """
    Class with all the necessary KZCash (KZC) testing network information based on
    https://github.com/kzcashteam/kzcash/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-kzcash'
    seeds = ('testdnsseed.kzcash.kz', )
    port = 18277
    message_start = b'\xcf\xe4\xcb\xca'
    base58_prefixes = {
        'PUBKEY_ADDR': 140,
        'SCRIPT_ADDR': 19,
        'SECRET_KEY': 239
    }
