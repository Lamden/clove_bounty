
from clove.network.bitcoin import Bitcoin


class SwagBucks(Bitcoin):
    """
    Class with all the necessary BUCKS network information based on
    http://www.github.com/pinkmagicdev/SwagBucks/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'swagbucks'
    symbols = ('BUCKS', )
    seeds = ('', '', )
    port = 1337
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 153
    }


class SwagBucksTestNet(SwagBucks):
    """
    Class with all the necessary BUCKS testing network information based on
    http://www.github.com/pinkmagicdev/SwagBucks/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-swagbucks'
    seeds = ()
    port = 2337
    message_start = b'\xcd\xf2\xc0\xef'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
