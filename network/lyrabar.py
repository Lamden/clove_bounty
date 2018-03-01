from clove.network.bitcoin import Bitcoin


class Lyrabar(Bitcoin):
    """
    Class with all the necessary Lyrabar network information based on
    https://github.com/Lyrabar/Lyrabar/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'lyrabar'
    symbols = ('LYB', )
    seeds = ("lyrabar.duckdns.org", "lyrabarpool.duckdns.org")
    port = 4046
    message_start = b'\x4d\x4d\x4d\x4d'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 176
    }

# no testnet
