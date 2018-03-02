from clove.network.bitcoin import Bitcoin


class DarkGold(Bitcoin):
    """
    Class with all the necessary DarkGold network information based on
    https://github.com/darkgoldcoin/darkgoldcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'darkgold'
    symbols = ('DGD', )
    seeds = ("seed1.Darkgold.eu", )
    port = 8855
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# no testnet
