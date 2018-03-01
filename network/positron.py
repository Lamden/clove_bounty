from clove.network.bitcoin import Bitcoin


class Positron(Bitcoin):
    """
    Class with all the necessary Positron network information based on
    https://github.com/SheepcoinDEV/Positron/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'positron'
    symbols = ('TRON', )
    seeds = ("seed.positron.ninja")
    port = 21454
    message_start = b'\xa4\xd2\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 183
    }

# no testnet
