
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


class SONOTestNet(SONO):
    """
    Class with all the necessary ALTCOM testing network information based on
    http://www.github.com/altcommunitycoin/altcommunitycoin-skunk/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-sono'
    seeds = ()
    port = 29844
    message_start = b'\x54\xac\xb3\xaa'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 193
    }
