from clove.network.bitcoin import Bitcoin


class RubleBit(Bitcoin):
    """
    Class with all the necessary RubleBit network information based on
    https://github.com/rublebit/rublebit/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'rublebit'
    symbols = ('RUBIT', )
    nodes = ("128.199.38.11", )
    port = 11333
    message_start = b'\xc3\xd2\xd1\xbd'
    base58_prefixes = {
        'PUBKEY_ADDR': 60,
        'SCRIPT_ADDR': 22,
        'SECRET_KEY': 188
    }


class RubleBitTestNet(RubleBit):
    """
    Class with all the necessary RubleBit testing network information based on
    https://github.com/rublebit/rublebit/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-rublebit'
    seeds = ("testnet-seed.ltc.xurious.com",
             "dnsseed.wemine-testnet.com")
    port = 11333
    message_start = b'\xd1\xb2\xa4\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 113,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 241
    }
