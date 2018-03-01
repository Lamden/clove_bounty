from clove.network.bitcoin import Bitcoin


class Trumpcoin(Bitcoin):
    """
    Class with all the necessary Trumpcoin (TRUMP) network information based on
    https://github.com/TRUMPCOIN/TRUMP/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'trumpcoin'
    symbols = ('TRUMP', )
    seeds = ('173.44.41.235', '178.33.84.2')
    port = 8468
    message_start = b'\xa6\xd2\xc3\xf6'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 193
    }


class TrumpcoinTestNet(Trumpcoin):
    """
    Class with all the necessary Trumpcoin (TRUMP) testing network information based on
    https://github.com/TRUMPCOIN/TRUMP/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-trumpcoin'
    seeds = ('173.44.41.235', )
    port = 18468
    message_start = b'\x3c\x4a\x2c\x1c'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
