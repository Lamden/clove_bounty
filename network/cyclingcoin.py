from clove.network.bitcoin import Bitcoin


class CyclingCoin(Bitcoin):
    """
    Class with all the necessary CYC network information based on
    https://github.com/cyclingcoin/cyclingcoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'cyclingcoin'
    symbols = ('CYC', )
    seeds = ()
    port = 15394
    message_start = b'\x05\x33\x19\x7B'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 117,
        'SECRET_KEY': 153
    }


class CyclingCoinTestNet(CyclingCoin):
    """
    Class with all the necessary CYC testing network information based on
    https://github.com/cyclingcoin/cyclingcoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-cyclingcoin'
    seeds = ()
    port = 15494
    message_start = b'\x03\x37\x1f\x21'
    base58_prefixes = {
        'PUBKEY_ADDR': 125,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
