from clove.network.bitcoin import Bitcoin


class Revenu(Bitcoin):
    """
    Class with all the necessary Revenu network information based on
    https://github.com/Revenu/revenu-source/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'revenu'
    symbols = ('REV', )
    seeds = ("node.walletbuilders.com")
    port = 6411
    message_start = b'\xd3\xf8\x65\x10'
    base58_prefixes = {
        'PUBKEY_ADDR': 60,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 188
    }

# no testnet
