from clove.network.bitcoin import Bitcoin


class GravityBit(Bitcoin):
    """
    Class with all the necessary GravityBit network information based on
    https://github.com/GravityBits/GravityBits/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'diamond'
    symbols = ('GBIT', )
    seeds = ("162.243.17.197",
             "159.203.126.200")
    port = 49011
    message_start = b'\xa4\xd2\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 166
    }
