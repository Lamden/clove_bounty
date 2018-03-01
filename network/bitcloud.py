
from clove.network.bitcoin import Bitcoin


class Bitcloud(Bitcoin):
    """
    Class with all the necessary BTDX network information based on
    http://www.github.com/LIMXTEC/Bitcloud/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'bitcloud'
    symbols = ('BTDX', )
    seeds = ('188.68.52.172', '37.120.186.85', '37.120.190.76')
    port = 8329
    message_start = b'\xe4\xe8\xbd\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 153
    }


class BitcloudTestNet(Bitcloud):
    """
    Class with all the necessary BTDX testing network information based on
    http://www.github.com/LIMXTEC/Bitcloud/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-bitcloud'
    seeds = ('188.68.52.172', '37.120.186.85', '37.120.190.76')
    port = 51474
    message_start = b'\x45\x76\x65\xba'
    base58_prefixes = {
        'PUBKEY_ADDR': 139,
        'SCRIPT_ADDR': 19,
        'SECRET_KEY': 239
    }
