from clove.network.bitcoin import Bitcoin


class BigCoin(Bitcoin):
    """
    Class with all the necessary BigCoin network information based on
    https://github.com/bigcoin/bigcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bigcoin'
    symbols = ('HUGE', )
    seeds = ("bigcoin.org", )
    port = 55884
    message_start = b'\xfc\xd9\xb7\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 10,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 138
    }

# Has no testnet
