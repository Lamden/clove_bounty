from clove.network.bitcoin import Bitcoin


class Winecoin(Bitcoin):
    """
    Class with all the necessary Winecoin network information based on
    https://github.com/winecoindev/winecoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'winecoin'
    symbols = ('WINE', )
    nodes = ("198.199.90.93", )
    port = 18473
    message_start = b'\xba\xf2\xe3\xf5'
    base58_prefixes = {
        'PUBKEY_ADDR': 73,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 201
    }

# no testnet
