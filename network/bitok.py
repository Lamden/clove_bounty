
from clove.network.bitcoin import Bitcoin


class Bitok(Bitcoin):
    """
    Class with all the necessary BITOK network information based on
    http://www.github.com/bitokproject/bitok/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'bitok'
    symbols = ('BITOK', )
    seeds = ('seed.bitok.online', 'seed2.bitok.online', 'seed3.bitok.online', )
    port = 11122
    message_start = b'\xbc\xa3\xfb\x5c'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 191,
        'SECRET_KEY': 125
    }


class BitokTestNet(Bitok):
    """
    Class with all the necessary BITOK testing network information based on
    http://www.github.com/bitokproject/bitok/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-bitok'
    seeds = ()
    port = 21997
    message_start = b'\xa7\xb1\xa5\xab'
    base58_prefixes = {
        'PUBKEY_ADDR': 127,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 255
    }
