
from clove.network.bitcoin import Bitcoin


class CannabisCoin(Bitcoin):
    """
    Class with all the necessary CANN network information based on
    http://www.github.com/cannabiscoindev/cannabiscoin420/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'cannabiscoin'
    symbols = ('CANN', )
    seeds = ('seed.cannabiscoin.net', 'seed2.cannabiscoin.net', )
    port = 39348
    message_start = b'\xfe\xc3\xb9\xde'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 156
    }


class CannabisCoinTestNet(CannabisCoin):
    """
    Class with all the necessary CANN testing network information based on
    http://www.github.com/cannabiscoindev/cannabiscoin420/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-cannabiscoin'
    seeds = ('testnet-seed.cannabiscoin.net', )
    port = 29347
    message_start = b'\xfe\xc4\xba\xde'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
