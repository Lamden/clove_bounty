from clove.network.bitcoin import Bitcoin


class AnalCoin(Bitcoin):
    """
    Class with all the necessary AnalCoin network information based on
    https://github.com/analcoin/analcoin/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'analcoin'
    symbols = ('ANAL', )
    nodes = ("108.61.178.105", )
    port = 4669
    message_start = b'\xf5\xe2\xf7\xb1'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 151
    }


# Has no testnet
