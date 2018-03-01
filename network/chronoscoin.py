from clove.network.bitcoin import Bitcoin


class Chronos(Bitcoin):
    """
    Class with all the necessary Chronos network information based on
    https://github.com/chronoscoin/Chronoscoin/blob/Coin/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'chronos'
    symbols = ('CRX', )
    nodes = ("199.127.226.174",
             "89.207.129.108")
    port = 7633
    message_start = b'\xe7\xf0\x1a\x8a'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 156
    }

# Has no testnet
