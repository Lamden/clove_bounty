from clove.network.bitcoin import Bitcoin


class Conquestcoin(Bitcoin):
    """
    Class with all the necessary Conquestcoin network information based on
    https://github.com/jlong187/conquestcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'conquestcoin'
    symbols = ('CQST', )
    nodes = ("216.31.12.30", )
    port = 7837
    message_start = b'\xf0\xc1\xdb\xfa'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 55,
        'SECRET_KEY': 156
    }

# Has no testnet
