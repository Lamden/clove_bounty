from clove.network.bitcoin import Bitcoin


class Firecoin(Bitcoin):
    """
    Class with all the necessary Firecoin network information based on
    https://github.com/firecoinx/Firecoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'firecoin'
    symbols = ('FIRE', )
    nodes = ("23.254.97.249", )
    port = 49697
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 163
    }

# no testnet
