from clove.network.bitcoin import Bitcoin


class Twelve(Bitcoin):
    """
    Class with all the necessary Twelve network information based on
    https://github.com/T-Inside/twelve/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'twelve'
    symbols = ('TWLV', )
    nodes = ("46.101.21.51",
             "46.101.155.214")
    port = 29662
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 105,
        'SECRET_KEY': 193
    }
