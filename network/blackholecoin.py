from clove.network.bitcoin import Bitcoin


class BlackholeCoin(Bitcoin):
    """
    Class with all the necessary BlackholeCoin network information based on
    https://github.com/blackholecoin/blackholecoin-master/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'diamond'
    symbols = ('BHC', )
    seeds = ("148.153.8.154",
             "38.121.61.46",
             "38.123.100.66",
             "148.153.8.50",
             "blackholecoin.io",
             "blackholecoin.com",
             "blackholecoin.org")
    port = 19100
    message_start = b'\xee\xd9\xf3\xf1'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# Has no testnet
