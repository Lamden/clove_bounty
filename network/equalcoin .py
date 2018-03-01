from clove.network.bitcoin import Bitcoin


class EqualCoin(Bitcoin):
    """
    Class with all the necessary EqualCoin network information based on
    https://github.com/equalcoinproject/equalcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'equalcoin'
    symbols = ('EQUAL', )
    nodes = ("216.31.12.38",
             "216.31.12.99")
    port = 13787
    message_start = b'\xc3\xda\xf1\xfb'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 81,
        'SECRET_KEY': 161
    }
