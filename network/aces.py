from clove.network.bitcoin import Bitcoin


class Aces(Bitcoin):
    """
    Class with all the necessary Aces network information based on
    https://www.github.com/aces-coin/acescoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Acesc'
    symbols = ('ACES', )
    seeds = ('81.4.123.155')
    port = 21274
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 151
    }
