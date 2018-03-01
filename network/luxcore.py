
from clove.network.bitcoin import Bitcoin


class Luxcore(Bitcoin):
    """
    Class with all the necessary LUX network information based on
    https://github.com/216k155/lux/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'luxcore'
    symbols = ('LUX', )
    seeds = ('5.189.142.181', '5.77.44.147', '209.250.254.156', '45.76.114.209',
             'luxseed1.luxcore.io', 'luxseed2.luxcore.io', 'luxseed3.luxcore.io', 'luxseed4.luxcore.io',)
    port = 26868
    message_start = b'\xf9\x73\xc9\xa7'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 48,
        'SECRET_KEY': 155
    }


class LuxcoreTestNet(Luxcore):
    """
    Class with all the necessary LUX testing network information based on
    https://github.com/216k155/lux/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'luxtest1'
    seeds = ('88.198.192.110',)
    port = 28333
    message_start = b'\x54\x67\x56\xab'
    base58_prefixes = {
        'PUBKEY_ADDR': 139,
        'SCRIPT_ADDR': 19,
        'SECRET_KEY': 239
    }
