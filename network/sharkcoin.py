
from clove.network.bitcoin import Bitcoin


class Sharkcoin(Bitcoin):
    """
    Class with all the necessary SAK network information based on
    http://www.github.com/shark-git/sharkcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'sharkcoin'
    symbols = ('SAK', )
    seeds = ('seed1.sak.cc', 'seed2.sak.cc', )
    port = 4011
    message_start = b'\xfe\xa5\x03\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 9,
        'SECRET_KEY': 191
    }
