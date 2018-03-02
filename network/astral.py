from clove.network.bitcoin import Bitcoin


class Astral(Bitcoin):
    """
    Class with all the necessary Astral network information based on
    https://github.com/astralcoindev/ASTRAL/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'astral'
    symbols = ('AST', )
    nodes = ("2.62.25.198", )
    port = 96755
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 9,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 137
    }

# Has no testnet
