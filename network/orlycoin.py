from clove.network.bitcoin import Bitcoin


class Orlycoin(Bitcoin):
    """
    Class with all the necessary Orlycoin network information based on
    https://github.com/Orlycoin/Orlycoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'orlycoin'
    symbols = ('ORLY', )
    seeds = ("158.69.159.45")
    port = 23452
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 115,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 243
    }

# no testnet
