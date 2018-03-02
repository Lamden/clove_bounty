from clove.network.bitcoin import Bitcoin


class Luxmi(Bitcoin):
    """
    Class with all the necessary Luxmi network information based on
    https://github.com/luxmicoin/Luxmi/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'luxmi'
    symbols = ('LXM', )
    seeds = ("luxmi.point2this.com", )
    port = 42192
    message_start = b'\xe3\xa7\x7c\x0e'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 176
    }

# no testnet
