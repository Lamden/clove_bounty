from clove.network.bitcoin import Bitcoin


class EneCoin(Bitcoin):
    """
    Class with all the necessary EneCoin network information based on
    https://github.com/die-ene/enecoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'enecoin'
    symbols = ('ENE', )
    seeds = ("52.37.214.176")
    port = 12124
    message_start = b'\x72\x35\xa4\xbd'
    base58_prefixes = {
        'PUBKEY_ADDR': 12,
        'SCRIPT_ADDR': 24,
        'SECRET_KEY': 140
    }

# no testnet
