
from clove.network.bitcoin import Bitcoin


class Signatum(Bitcoin):
    """
    Class with all the necessary SIGT network information based on
    http://www.github.com/signatumd/source/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'signatum'
    symbols = ('SIGT', )
    seeds = ('54.175.225.242',)
    port = 33333
    message_start = b'\xef\xf2\xa7\x7d'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 191
    }


class SignatumTestNet(Signatum):
    """
    Class with all the necessary SIGT testing network information based on
    http://www.github.com/signatumd/source/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-signatum'
    seeds = ('122.129.64.13', '122.129.64.14', '122.129.64.15', '122.129.64.16',
             '203.128.6.219', '216.155.145.167', '45.32.102.240', '45.77.51.253', '107.22.138.243')
    port = 26178
    message_start = b'\x71\x31\x21\x11'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 193
    }
