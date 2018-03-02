from clove.network.bitcoin import Bitcoin


class Saffroncoin(Bitcoin):
    """
    Class with all the necessary Saffroncoin network information based on
    https://github.com/saffroncoin/saffroncoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'saffroncoin'
    symbols = ('SFR', )
    seeds = ("saffroncoin.com", )
    port = 19717
    message_start = b'\xcf\x05\x67\xea'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 177
    }


class SaffroncoinTestNet(Saffroncoin):
    """
    Class with all the necessary Saffroncoin testing network information based on
    https://github.com/saffroncoin/saffroncoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-saffroncoin'
    seeds = ("testseed1.saffroncoin.org", )
    port = 29717
    message_start = b'\x01\xf5\x55\xa4'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 188,
        'SECRET_KEY': 239
    }
