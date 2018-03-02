from clove.network.bitcoin import Bitcoin


class Aces(Bitcoin):
    """
    Class with all the necessary  Aces (ACES) network information based on
    https://github.com/aces-coin/AcesCoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'aces'
    symbols = ('ACES', )
    nodes = ('81.4.123.155', )
    port = 21274
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 151
    }


class AcesTestNet(Aces):
    """
    Class with all the necessary  Aces (ACES) network information based on
    https://github.com/aces-coin/AcesCoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-aces'
    symbols = ('ACES', )
    nodes = ()
    port = 21275
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
