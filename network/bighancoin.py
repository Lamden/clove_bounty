from clove.network.bitcoin import Bitcoin


class BighanCoin(Bitcoin):
    """
    Class with all the necessary BighanCoin network information based on
    https://github.com/bighancoin/bighancoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bighancoin'
    symbols = ('BHC', )
    nodes = (
        "47.90.14.128", "139.196.140.101"
    )
    port = 29720
    message_start = b'\xfe\xa5\x03\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 9,
        'SECRET_KEY': 153
    }

# Has no testnet
