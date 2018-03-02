
from clove.network.bitcoin import Bitcoin


class Numus(Bitcoin):
    """
    Class with all the necessary NMS network information based on
    http://www.github.com/numuscrypto/numuscore/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'numus'
    symbols = ('NMS', )
    nodes = ('141.255.161.78', '143.202.154.31', )
    port = 28121
    message_start = b'\xf1\xec\xa1\xc7'
    base58_prefixes = {
        'PUBKEY_ADDR': 21,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 25
    }


class NumusTestNet(Numus):
    """
    Class with all the necessary NMS testing network information based on
    http://www.github.com/numuscrypto/numuscore/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-numus'
    seeds = ()
    port = 27121
    message_start = b'\x1f\x22\x05\x30'
    base58_prefixes = {
        'PUBKEY_ADDR': 45,
        'SCRIPT_ADDR': 44,
        'SECRET_KEY': 50
    }
