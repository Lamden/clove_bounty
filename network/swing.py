from clove.network.bitcoin import Bitcoin


class Swing(Bitcoin):
    """
    Class with all the necessary Swing network information based on
    https://github.com/swingcoin/swing/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'swing'
    symbols = ('SWING', )
    seeds = ("swing.suprnova.cc", )
    port = 16061
    message_start = b'\xdd\x1e\xe2\xaf'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 191
    }


# Has no testnet
