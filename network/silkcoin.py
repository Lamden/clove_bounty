from clove.network.bitcoin import Bitcoin


class Silkcoin(Bitcoin):
    """
    Class with all the necessary Silkcoin network information based on
    https://github.com/shnurf/silkcoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'silkcoin'
    symbols = ('SILK', )
    nodes = ("107.170.61.197", "107.170.73.238", )
    port = 16666
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# no testnet
