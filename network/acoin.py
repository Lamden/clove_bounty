from clove.network.bitcoin import Bitcoin


class Acoin(Bitcoin):
    """
    Class with all the necessary  Acoin (ACOIN) network information based on
    https://github.com/acoin-project/acoin/blob/master/src/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'acoin'
    symbols = ('ACOIN', )
    seeds = ('seed1.a-coin.info', 'seed2.a-coin.info', 'seed3.a-coin.info', 'seed4.a-coin.info',
             'seed5.a-coin.info', 'seed6.a-coin.info', 'seed7.a-coin.info', 'seed8.a-coin.info')
    port = 17883
    message_start = b'\xfb\xb5\x05\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 10,
        'SECRET_KEY': 230
    }


class AcoinTestNet(Acoin):
    """
    Class with all the necessary  Acoin (ACOIN) network information based on
    https://github.com/acoin-project/acoin/blob/master/src/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-acoin'
    symbols = ('ACOIN', )
    seeds = ()
    port = 27883
    message_start = b'\x1a\xee\xa5\x0d'
    base58_prefixes = {
        'PUBKEY_ADDR': 87,
        'SCRIPT_ADDR': 187,
        'SECRET_KEY': 238
    }
