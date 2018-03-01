from clove.network.bitcoin import Bitcoin


class GIZMOcoin(Bitcoin):
    """
    Class with all the necessary GIZMOcoin network information based on
    https://github.com/GIZMOcoinTEAM/SourceCode/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'gizmocoin'
    symbols = ('GIZ', )
    seeds = ("45.55.134.78", "45.55.130.228")
    port = 18700
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 166
    }

# no testnet
