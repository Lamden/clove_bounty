from clove.network.bitcoin import Bitcoin


class Obscurebay(Bitcoin):
    """
    Class with all the necessary Obscurebay network information based on
    https://github.com/donotforgetnever/obscurebay/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'obscurebay'
    symbols = ('OBS', )
    seeds = ("54.149.102.226")
    port = 47458
    message_start = b'\xf3\x2d\xa5\x71'
    base58_prefixes = {
        'PUBKEY_ADDR': 115,
        'SCRIPT_ADDR': 142,
        'SECRET_KEY': 243
    }

# no testnet
