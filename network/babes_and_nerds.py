from clove.network.bitcoin import Bitcoin


class BabesAndNerds(Bitcoin):
    """
    Class with all the necessary Babes and Nerds network information based on
    https://github.com/marksize/lowered/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'babes_and_nerds'
    symbols = ('ban', )
    nodes = ("52.88.144.119", )
    port = 44258
    message_start = b'\xf3\x2d\xa5\x71'
    base58_prefixes = {
        'PUBKEY_ADDR': 21,
        'SCRIPT_ADDR': 142,
        'SECRET_KEY': 149
    }

# no testnet
