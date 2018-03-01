
from clove.network.bitcoin import Bitcoin


class Sparks(Bitcoin):
    """
    Class with all the necessary SPK network information based on
    https://github.com/sparkscrypto/Sparks/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'sparks'
    symbols = ('SPK', )
    seeds = (
        'seed.sparks.gold',
        'explorer.sparks.gold'
    )
    port = 8890
    message_start = b'\x1a\xb2\xc3\xd4'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 10,
        'SECRET_KEY': 198
    }


class SparksTestNet(Sparks):
    """
    Class with all the necessary SPK testing network information based on
    https://github.com/sparkscrypto/Sparks/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-sparks'
    seeds = ()
    port = 8891
    message_start = b'\xd1\x2b\xb3\x7a'
    base58_prefixes = {
        'PUBKEY_ADDR': 112,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 240
    }
