from clove.network.bitcoin import Bitcoin


class ScryptToken(Bitcoin):
    """
    Class with all the necessary ScryptToken network information based on
    https://github.com/coolindark/ScryptToken/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'scrypttoken'
    symbols = ('SCT', )
    nodes = ("5.135.29.200",
             "172.245.62.6")
    port = 7921
    message_start = b'\x10\xb1\xc5\xc2'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 191
    }

# no testnet
