from clove.network.bitcoin import Bitcoin


class Impact(Bitcoin):
    """
    Class with all the necessary Impact network information based on
    https://github.com/Impactcoin/Impactcoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'impact'
    symbols = ('IMX', )
    nodes = ("194.135.85.185", )
    port = 17771
    message_start = b'\xb1\xf5\xd3\xa9'
    base58_prefixes = {
        'PUBKEY_ADDR': 76,
        'SCRIPT_ADDR': 141,
        'SECRET_KEY': 204
    }

# no testnet
