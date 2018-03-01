
from clove.network.bitcoin import Bitcoin


class CthulhuOfferings(Bitcoin):
    """
    Class with all the necessary OFF network information based on
    http://www.github.com/thegreatoldone/offerings/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'cthulhuofferings'
    symbols = ('OFF', )
    nodes = ('144.76.91.109', )
    port = 20000
    message_start = b'\xfe\xa5\x03\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 58,
        'SCRIPT_ADDR': 9,
        'SECRET_KEY': 186
    }


class CthulhuOfferingsTestNet(CthulhuOfferings):
    """
    Class with all the necessary OFF testing network information based on
    http://www.github.com/thegreatoldone/offerings/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-cthulhuofferings'
    seeds = ('', )
    port = 21973
    message_start = b'\x01\x1a\x39\xf7'
    base58_prefixes = {
        'PUBKEY_ADDR': 119,
        'SCRIPT_ADDR': 199,
        'SECRET_KEY': 247
    }
