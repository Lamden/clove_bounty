from clove.network.bitcoin import Bitcoin


class Graviton(Bitcoin):
    """
    Class with all the necessary Graviton network information based on
    https://github.com/gravitondev/graviton/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'graviton'
    symbols = ('GRAV', )
    seeds = ("seed.graviton.ninja")
    port = 31321
    message_start = b'\xcd\x1f\x3a\x2d'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# no testnet
