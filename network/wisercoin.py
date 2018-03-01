from clove.network.bitcoin import Bitcoin


class WiserCoin(Bitcoin):
    """
    Class with all the necessary WiserCoin network information based on
    https://github.com/databir/WiserCoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'wisercoin'
    symbols = ('WSC', )
    seeds = ("sec1.wisercoin.com",
             "sec2.wisercoin.com")
    port = 21777
    message_start = b'\x21\x13\x23\xe9'
    base58_prefixes = {
        'PUBKEY_ADDR': 73,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 201
    }
