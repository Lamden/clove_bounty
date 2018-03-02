from clove.network.bitcoin import Bitcoin


class RipoffCoin(Bitcoin):
    """
    Class with all the necessary RipoffCoin network information based on
    https://github.com/RipoffCoin/RipoffCoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'ripoffcoin'
    symbols = ('RIPO', )
    seeds = ("seed.ripoffcoin.com", )
    port = 54001
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 60,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 188
    }


class RipoffCoinTestNet(RipoffCoin):
    """
    Class with all the necessary RipoffCoin testing network information based on
    https://github.com/RipoffCoin/RipoffCoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-ripoffcoin'
    seeds = ("seedtest.ripoffcoin.com", )
    port = 54002
    message_start = b'\xfc\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 122,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 250
    }
