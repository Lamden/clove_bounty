from clove.network.bitcoin import Bitcoin


class Cinni(Bitcoin):
    """
    Class with all the necessary Cinni network information based on
    https://github.com/Cinnicoin/CinniCoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'cinni'
    symbols = ('CINNI', )
    seeds = ("108.61.103.46")
    port = 31813
    message_start = b'\xce\xfb\xfa\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 43,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 171
    }

# Has no testnet
