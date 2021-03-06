from clove.network.bitcoin import Bitcoin


class Lycancoin(Bitcoin):
    """
    Class with all the necessary Lycancoin network information based on
    https://github.com/lycancoin/lycancoin-release/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'lycancoin'
    symbols = ('LYC', )
    nodes = ("69.172.229.161", "209.208.111.72", )
    port = 58862
    message_start = b'\xfc\xd9\xb7\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 176
    }
