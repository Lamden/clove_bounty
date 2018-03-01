from clove.network.bitcoin import Bitcoin


class YamahaCoin(Bitcoin):
    """
    Class with all the necessary YamahaCoin network information based on
    https://github.com/yamahacoin/ymc-source/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'yamahacoin'
    symbols = ('YMC', )
    seeds = ("node.walletbuilders.com", )
    port = 8003
    message_start = b'\x1b\x6d\x06\x34'
    base58_prefixes = {
        'PUBKEY_ADDR': 78,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 206
    }

# no testnet
