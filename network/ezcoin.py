from clove.network.bitcoin import Bitcoin


class EZCoin(Bitcoin):
    """
    Class with all the necessary EZCoin network information based on
    https://github.com/ezcoin/ezcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'ezcoin'
    symbols = ('EZC', )
    seeds = ("ezcoin1.chickenkiller.com",
             "ezcoin.ignorelist.com",
             "ezcoin.mooo.com",
             "ezcoin.strangled.net")
    port = 7955
    message_start = b'\xfe\xc3\xa5\xdf'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 161
    }


class EZCoinTestNet(EZCoin):
    """
    Class with all the necessary EZCoin testing network information based on
    https://github.com/ezcoin/ezcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-ezcoin'
    seeds = ("testseed1.ezcoin.org")
    port = 17955
    message_start = b'\xf2\xc5\xa7\xde'
    base58_prefixes = {
        'PUBKEY_ADDR': 44,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 172
    }
