from clove.network.bitcoin import Bitcoin


class Fibre(Bitcoin):
    """
    Class with all the necessary Fibre network information based on
    https://github.com/fibre-team/fibre-public/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'fibre'
    symbols = ('FIBRE', )
    seeds = ("seed1.worldfibre.net",
             "seed2.worldfibre.net",
             "seed3.worldfibre.net",
             "seed4.worldfibre.net",
             "seed5.worldfibre.net")
    port = 7223
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 163
    }

# no testnet
