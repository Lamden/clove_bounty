
from clove.network.bitcoin import Bitcoin


class Espers(Bitcoin):
    """
    Class with all the necessary ESP network information based on
    http://www.github.com/cryptocoderz/espers/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'espers'
    symbols = ('ESP', )
    seeds = ('esp.cryptocoderz.com', )
    port = 22448
    message_start = b'\x4e\xaa\x32\x1c'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 92,
        'SECRET_KEY': 144
    }
