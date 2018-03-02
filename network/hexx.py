from clove.network.bitcoin import Bitcoin


class Hexx(Bitcoin):
    """
    Class with all the necessary Hexx network information based on
    https://github.com/hexxcointakeover/hexxcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'hexx'
    symbols = ('HXX', )
    seeds = ("76.74.170.249")
    port = 29100
    message_start = b'hexx'
    base58_prefixes = {
        'PUBKEY_ADDR': 40,
        'SCRIPT_ADDR': 100,
        'SECRET_KEY': 168
    }

# no testnet
