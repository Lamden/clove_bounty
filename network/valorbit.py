
from clove.network.bitcoin import Bitcoin


class Valorbit(Bitcoin):
    """
    Class with all the necessary VAL network information based on
    http://www.github.com/valorbit/valorbit/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'valorbit'
    symbols = ('VAL', )
    seeds = ('seed.valorbit.com', 'seed2.valorbit.com',
             'seed3.valorbit.com', 'seed.dblore.com', 'seed2.dblore.com')
    port = 8338
    message_start = b'\xcf\xd1\xe8\xea'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }
