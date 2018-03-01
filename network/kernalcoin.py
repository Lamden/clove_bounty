from clove.network.bitcoin import Bitcoin


class Kernalcoin(Bitcoin):
    """
    Class with all the necessary Kernalcoin network information based on
    https://github.com/kernalcoin/Kernal/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'kernalcoin'
    symbols = ('KC', )
    nodes = ("45.63.71.91", )
    port = 4769
    message_start = b'\xf5\xe2\xf7\xb1'
    base58_prefixes = {
        'PUBKEY_ADDR': 46,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 174
    }

# no testnet
