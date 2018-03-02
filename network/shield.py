from clove.network.bitcoin import Bitcoin


class Shield(Bitcoin):
    """
    Class with all the necessary Shield network information based on
    https://github.com/ShieldCoin/SHIELD/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'shield'
    symbols = ('XSH', )
    seeds = ("electrum-1.shieldcurrency.com",
             "electrum-1.shieldcurrency.com")
    port = 21103
    message_start = b'\xa1\xb3\xc4\xee'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 33,
        'SECRET_KEY': 191
    }

# no testnet
