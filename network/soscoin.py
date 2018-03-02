from clove.network.bitcoin import Bitcoin


class SOSCoin(Bitcoin):
    """
    Class with all the necessary SOSCoin network information based on
    https://github.com/soscoindev/sos/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'soscoin'
    symbols = ('SOS', )
    seeds = ("node.walletbuilders.com", )
    port = 7599
    message_start = b'\x20\xab\x81\x22'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 191
    }

# no testnet
