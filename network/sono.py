
from clove.network.bitcoin import Bitcoin


class SONO(Bitcoin):
    """
    Class with all the necessary ALTCOM network information based on
    http://www.github.com/altcommunitycoin/altcommunitycoin-skunk/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'sono'
    symbols = ('ALTCOM', )
    seeds = ('zPools.de', )
    port = 29855
    message_start = b'\x4a\x12\x22\x14'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 191
    }
