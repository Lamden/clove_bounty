from clove.network.bitcoin import Bitcoin


class Swapcoin(Bitcoin):
    """
    Class with all the necessary Swapcoin network information based on
    https://github.com/swapcoin/swap/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'swapcoin'
    symbols = ('SWP', )
    nodes = ("207.12.89.115", )
    port = 19988
    message_start = b'\xbf\x0c\x6b\xbd'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 191
    }

# no testnet
