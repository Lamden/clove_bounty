
from clove.network.bitcoin import Bitcoin


class AdvancedInternetBlocks(Bitcoin):
    """
    Class with all the necessary AIB network information based on
    https://github.com/iobond/aib/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test'
    symbols = ('AIB', )
    seeds = ('seed.wtmint.com', 'seed.iobond.com', 'seed.aib.one', )
    port = 5223
    message_start = b'\xa3\xb1\xc4\xd1'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 151
    }
