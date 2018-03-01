from clove.network.bitcoin import Bitcoin


class Shitcoin(Bitcoin):
    """
    Class with all the necessary Shitcoin network information based on
    https://github.com/shit-coin/shit/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'shitcoin'
    symbols = ('SHIT', )
    nodes = ("172.245.173.137", )
    port = 9999
    message_start = b'\xf3\x2d\xa5\x71'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 187,
        'SECRET_KEY': 191
    }

# no testnet
