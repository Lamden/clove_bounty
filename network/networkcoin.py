from clove.network.bitcoin import Bitcoin


class Networkcoin(Bitcoin):
    """
    Class with all the necessary Networkcoin network information based on
    https://github.com/NETWORKCOIN/NETC-NETWORKCOINX_13/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'networkcoin'
    symbols = ('NETC', )
    nodes = ("45.63.5.183", )
    port = 19172
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 53,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 181
    }

# no testnet
