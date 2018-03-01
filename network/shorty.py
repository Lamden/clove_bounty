from clove.network.bitcoin import Bitcoin


class Shorty(Bitcoin):
    """
    Class with all the necessary Shorty network information based on
    https://github.com/shortysho/shorty/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'shorty'
    symbols = ('SHORTY', )
    nodes = ("35.163.38.207", )
    port = 28188
    message_start = b'\xf3\x2d\xa5\x71'
    base58_prefixes = {
        'PUBKEY_ADDR': 8,
        'SCRIPT_ADDR': 142,
        'SECRET_KEY': 136
    }

# no testnet
