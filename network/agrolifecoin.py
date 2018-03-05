from clove.network.bitcoin import Bitcoin


class AgrolifeCoin(Bitcoin):
    """
    Class with all the necessary  AgrolifeCoin (AGLC) network information based on
    https://github.com/traiborg/Agrolifecoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'agrolifecoin'
    symbols = ('AGLC', )
    seeds = ('seed.agrolifecoin.org', 'seed2.agrolifecoin.org', )
    port = 27330
    message_start = b'\xa4\x22\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 1,
        'SECRET_KEY': 151
    }
