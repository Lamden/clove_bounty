from clove.network.bitcoin import Bitcoin


class Pentacoin(Bitcoin):
    """
    Class with all the necessary Pentacoin network information based on
    https://github.com/penta2015/pentacoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'pentacoin'
    symbols = ('PTA', )
    nodes = ("104.236.199.148", )
    port = 25631
    message_start = b'\x4a\x2d\x8f\x6a'
    base58_prefixes = {
        'PUBKEY_ADDR': 56,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 184
    }

# no testnet
