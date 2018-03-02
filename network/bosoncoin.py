from clove.network.bitcoin import Bitcoin


class BosonCoin(Bitcoin):
    """
    Class with all the necessary BosonCoin network information based on
    https://github.com/bosonproject/Boson/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bosoncoin'
    symbols = ('BOSON', )
    nodes = ("45.42.189.74",
             "107.190.164.220")
    port = 12090
    message_start = b'\xf1\xc1\xfa\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 26,
        'SCRIPT_ADDR': 17,
        'SECRET_KEY': 154
    }
