from clove.network.bitcoin import Bitcoin


class Xtrabytes(Bitcoin):
    """
    Class with all the necessary Xtrabytes network information based on
    https://github.com/borzalom/xtrabytes/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Xtrabytes'
    symbols = ('XBY', )
    seeds = ("79.172.210.27", "79.172.210.45")
    port = 34002
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 153
    }


# Has no Testnet
