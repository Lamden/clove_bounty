
from clove.network.bitcoin import Bitcoin


class Voyacoin(Bitcoin):
    """
    Class with all the necessary VOYA network information based on
    http://www.github.com/Voyacoin/Voyacoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'voyacoin'
    symbols = ('VOYA', )
    seeds = ('104.43.195.20',)
    port = 12121
    message_start = b'\xa3\xb1\x03\xc2'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 43,
        'SECRET_KEY': 128
    }


class VoyacoinTestNet(Voyacoin):
    """
    Class with all the necessary VOYA testing network information based on
    http://www.github.com/Voyacoin/Voyacoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-voyacoin'
    seeds = ('104.43.195.20',)
    port = 22121
    message_start = b'\x3a\x1a\x0c\xab'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
