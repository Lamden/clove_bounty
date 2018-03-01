from clove.network.bitcoin import Bitcoin


class EggCoin(Bitcoin):
    """
    Class with all the necessary EGG network information based on
    https://github.com/eastercoindev/eggcoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'eggcoin'
    symbols = ('EGG', )
    seeds = ()
    port = 31104
    message_start = b'\x1a\x32\x03\x20'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }


class EggCoinTestNet(EggCoin):
    """
    Class with all the necessary EGG testing network information based on
    https://github.com/eastercoindev/eggcoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-eggcoin'
    seeds = ()
    port = 20134
    message_start = b'\x2a\x23\x06\x40'
    base58_prefixes = {
        'PUBKEY_ADDR': 127,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
