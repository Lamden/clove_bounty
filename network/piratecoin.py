from clove.network.bitcoin import Bitcoin


class PirateCoin(Bitcoin):
    """
    Class with all the necessary PirateCoin network information based on
    https://github.com/kebian/Piratecoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'piratecoin'
    symbols = ('PIR', )
    seeds = ("dnsseed.piratecoin.co")
    port = 17771
    message_start = b'\xdd\xb9\xb7\xef'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 151
    }

# no 11656
