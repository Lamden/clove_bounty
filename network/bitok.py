
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
