from clove.network.bitcoin import Bitcoin


class PoolStamp(Bitcoin):
    """
    Class with all the necessary PoolStamp network information based on
    https://github.com/poolstamp/poolstamp/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'poolstamp'
    symbols = ('XSP', )
    seeds = ("104.236.120.8", "188.166.56.148")
    port = 24662
    message_start = b'\xb1\xb0\xb2\xb3'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 183
    }

# no testnet
