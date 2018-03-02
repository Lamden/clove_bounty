from clove.network.bitcoin import Bitcoin


class SmartCash(Bitcoin):
    """
    Class with all the necessary SmartCash SMART network information based on
    https://github.com/SmartCash/smartcash/blob/1.1/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'smartcash'
    symbols = ('SMART', )
    seeds = ('seed.smrt.cash', 'seed1.smrt.cash', 'seed2.smrt.cash', 'seed1.smartcash.org', 'seed2.smartcash.org',
             'seed.smartcash.cc', 'seed2.smartcash.cc', 'seed3.smartcash.cc', 'seed4.smartcash.cc')
    port = 9678
    message_start = b'\x5c\xa1\xab\x1e'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 18,
        'SECRET_KEY': 191
    }


class SmartCashTestNet(SmartCash):
    """
    Class with all the necessary SmartCash SMART testing network information based on
    https://github.com/SmartCash/smartcash/blob/1.1/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-smartcash'
    seeds = ('testnet.smartcash.cc"', 'testnet.smrt.cash', )
    port = 19678
    message_start = b'\xcf\xfc\xbe\xea'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 21,
        'SECRET_KEY': 193
    }
