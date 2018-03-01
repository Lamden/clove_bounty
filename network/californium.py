
from clove.network.bitcoin import Bitcoin


class Californium(Bitcoin):
    """
    Class with all the necessary CF network information based on
    http://www.github.com/Californium/Californium/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'californium'
    symbols = ('CF', )
    seeds = ('54.149.30.199', '')
    port = 44252
    message_start = b'\x0f\xdb\xbb\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 88,
        'SCRIPT_ADDR': 30,
        'SECRET_KEY': 224
    }


class CaliforniumTestNet(Californium):
    """
    Class with all the necessary CF testing network information based on
    http://www.github.com/Californium/Californium/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-californium'
    seeds = ()
    port = 45530
    message_start = b'\x0f\xdb\xbb\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 68,
        'SCRIPT_ADDR': 30,
        'SECRET_KEY': 239
    }
