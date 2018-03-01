from clove.network.bitcoin import Bitcoin


class Bitswift(Bitcoin):
    """
    Class with all the necessary Bitswift network information based on
    https://github.com/BitSwift-v2/bitswift/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'Bitswift'
    symbols = ('SWIFT', )
    seeds = ("144.217.81.218",
             "144.217.4.246",
             "149.56.111.174",
             "144.217.15.225")
    port = 21138
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 85,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 213
    }

# Has no testnet
