from clove.network.bitcoin import Bitcoin


class Unfed(Bitcoin):
    """
    Class with all the necessary Unfed network information based on
    https://github.com/unfedcurrency/unfed/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'unfed'
    symbols = ('UNF', )
    seeds = ("52.36.161.129")
    port = 12387
    message_start = b'\xfd\xc1\xa5\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 68,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 196
    }

# no testnet
