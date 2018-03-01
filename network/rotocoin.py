from clove.network.bitcoin import Bitcoin


class RotoCoin(Bitcoin):
    """
    Class with all the necessary RotoCoin network information based on
    https://github.com/rotocoin/rotocoin/blob/roto-thegreat-win/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'rotocoin'
    symbols = ('RT2', )
    seeds = ("embi.zapto.org",
             "rt2.poolerino.com")
    port = 17771
    message_start = b'\xfa\xbf\xb5\xda'
    base58_prefixes = {
        'PUBKEY_ADDR': 61,
        'SCRIPT_ADDR': 123,
        'SECRET_KEY': 189
    }
