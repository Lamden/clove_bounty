from clove.network.bitcoin import Bitcoin


class Cyder(Bitcoin):
    """
    Class with all the necessary Cyder (CYDER) network information based on
    https://github.com/cyderenergy/cyder/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'cyder'
    symbols = ('CYDER', )
    nodes = ('34.212.55.142', )
    port = 48848
    message_start = b'\xf3\x2d\xa5\x71'
    base58_prefixes = {
        'PUBKEY_ADDR': 20,
        'SCRIPT_ADDR': 142,
        'SECRET_KEY': 148
    }

# no testnet
