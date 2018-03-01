from clove.network.bitcoin import Bitcoin


class DarkTron(Bitcoin):
    """
    Class with all the necessary DarkTron network information based on
    https://github.com/DarkTronDev/DarkTron/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'darktron'
    symbols = ('DRKT', )
    nodes = ("178.62.222.55", )
    port = 31454
    message_start = b'\xa4\xd2\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 12,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 140
    }

# has no testnet
