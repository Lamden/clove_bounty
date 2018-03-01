from clove.network.bitcoin import Bitcoin


class XxXcoin(Bitcoin):
    """
    Class with all the necessary XxXcoin network information based on
    https://github.com/devxxxcoin/xxxcoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'xxxcoin'
    symbols = ('XXX', )
    nodes = ("85.214.147.99", )
    port = 20133
    message_start = b'\xce\xfb\xeb\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 75,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 203
    }

# no testnet
