from clove.network.bitcoin import Bitcoin


class Yenten(Bitcoin):
    """
    Class with all the necessary  Yenten (YTN) network information based on
    https://github.com/conan-equal-newone/yenten/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'yenten'
    symbols = ('YTN', )
    seeds = ('seed.yenten.org')
    port = 9981
    message_start = b'\xad\x5a\xeb\x9f'
    base58_prefixes = {
        'PUBKEY_ADDR': 78,
        'SCRIPT_ADDR': 10,
        'SECRET_KEY': 123
    }


class YentenTestNet(Yenten):
    """
    Class with all the necessary  Yenten (YTN) network information based on
    https://github.com/conan-equal-newone/yenten/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-yenten'
    symbols = ('YTN', )
    seeds = ()
    port = 19981
    message_start = b'\x95\x54\xe4\x95'
    base58_prefixes = {
        'PUBKEY_ADDR': 112,
        'SCRIPT_ADDR': 197,
        'SECRET_KEY': 240
    }
