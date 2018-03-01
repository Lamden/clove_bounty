from clove.network.bitcoin import Bitcoin


class Litecred(Bitcoin):
    """
    Class with all the necessary Litecred network information based on
    https://github.com/Litecred-Project/Litecred/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'litecred'
    symbols = ('LTCR', )
    seeds = ("litenode1.litecred.org",
             "litenode2.litecred.org")
    port = 8868
    message_start = b'\x2d\x3f\xa2\xf5'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }
