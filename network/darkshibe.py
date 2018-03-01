from clove.network.bitcoin import Bitcoin


class DarkShibe(Bitcoin):
    """
    Class with all the necessary DarkShibe network information based on
    https://github.com/DarkShibe/DarkShibe/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'DarkShibe'
    symbols = ('DSB', )
    nodes = ("104.131.102.57",
             "104.131.102.91")
    port = 54312
    message_start = b'\xfb\xf5\xff\xfa'
    base58_prefixes = {
        'PUBKEY_ADDR': 30,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 158
    }
