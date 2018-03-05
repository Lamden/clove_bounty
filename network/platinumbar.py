
from clove.network.bitcoin import Bitcoin


class PlatinumBAR(Bitcoin):
    """
    Class with all the necessary XPTX network information based on
    http://www.github.com/xptx/PlatinumBar/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'platinumbar'
    symbols = ('XPTX', )
    seeds = ('seed1.platinumbar.io', 'seed2.platinumbar.io',
             'seed3.platinumbar.io', 'seed4.platinumbar.io', 'seed5.platinumbar.io')
    port = 18993
    message_start = b'\x03\x03\x06\x06'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 117,
        'SECRET_KEY': 214
    }
