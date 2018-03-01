from clove.network.bitcoin import Bitcoin


class NumbersCoin(Bitcoin):
    """
    Class with all the necessary NumbersCoin network information based on
    https://github.com/numberscoin/num/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'numberscoin'
    symbols = ('NUM', )
    seeds = ("node.walletbuilders.com", )
    port = 6975
    message_start = b'\x42\x22\xae\x3c'
    base58_prefixes = {
        'PUBKEY_ADDR': 53,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 181
    }

# no testnet
