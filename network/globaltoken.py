from clove.network.bitcoin import Bitcoin


class GlobalToken(Bitcoin):
    """
    Class with all the necessary GlobalToken (GLT) network information based on
    https://github.com/globaltoken/globaltoken/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'globaltoken'
    symbols = ('GLT', )
    seeds = ('lameserver.de', )
    port = 9319
    message_start = b'\xc7\x08\xd3\x2d'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 166
    }


class GlobalTokenTestNet(GlobalToken):
    """
    Class with all the necessary GlobalToken (GLT) testing network information based on
    https://github.com/globaltoken/globaltoken/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-globaltoken'
    seeds = ()
    nodes = ('134.255.221.7', )
    port = 19319
    message_start = b'\x3a\x6f\x37\x5b'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
