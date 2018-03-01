
from clove.network.bitcoin import Bitcoin


class i0coin(Bitcoin):
    """
    Class with all the necessary I0C network information based on
    http://www.github.com/domob1812/i0coin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'i0coin'
    symbols = ('I0C', )
    seeds = ('seed.i0coin.domob.eu',)
    port = 7333
    message_start = b'\xf1\xb2\xb3\xd4'
    base58_prefixes = {
        'PUBKEY_ADDR': 105,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


class i0coinTestNet(i0coin):
    """
    Class with all the necessary I0C testing network information based on
    http://www.github.com/domob1812/i0coin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-i0coin'
    seeds = ()
    port = 17333
    message_start = b'\x0b\x11\x09\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 112,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
