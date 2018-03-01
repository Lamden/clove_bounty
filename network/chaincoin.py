from clove.network.bitcoin import Bitcoin


class Chaincoin(Bitcoin):
    """
    Class with all the necessary CHC network information based on
    https://github.com/chaincoin/chaincoin/blob/master/src/chainparams.cpp
    (date of access: 01/18/2018)
    """
    name = 'chaincoin'
    symbols = ('CHC', )
    seeds = (
        'seed1.chaincoin.org',
        'seed2.chaincoin.org',
        'seed3.chaincoin.org',
        'seed4.chaincoin.org',
        'seed5.chaincoin.org',
        'seed6.chaincoin.org',
        'seed7.chaincoin.org',
        'seed8.chaincoin.org',
        'chc1.ignorelist.com',
        'chc2.ignorelist.com',
        'chc3.ignorelist.com',
        'chc4.ignorelist.com',
    )
    port = 11994
    message_start = b'\xf9\xbe\xb4\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


# Chaincoin does not have a TESTNET
# https://github.com/chaincoin/chaincoin/blob/master/src/chainparams.cpp#L147
