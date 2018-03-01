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
             "209.250.241.56",
             "45.77.230.110",
             "45.32.36.108",
             "199.247.6.151",
             "198.13.33.179",
             "electrum-1.shieldcurrency.com")
    port = 21103
    message_start = b'\xa1\xb3\xc4\xee'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 33,
        'SECRET_KEY': 191
    }

# no testnet
