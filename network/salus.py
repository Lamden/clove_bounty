
from clove.network.bitcoin import Bitcoin


class SaluS(Bitcoin):
    """
    Class with all the necessary SLS network information based on
    http://www.github.com/saluscoin/SaluS/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'salus'
    symbols = ('SLS', )
    seeds = ('198.50.243.69',)
    port = 22534
    message_start = b'\xd3\xc5\xa7\x21'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 23,
        'SECRET_KEY': 191
    }


class SaluSTestNet(SaluS):
    """
    Class with all the necessary SLS testing network information based on
    http://www.github.com/saluscoin/SaluS/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-salus'
    seeds = ()
    port = 55937
    message_start = b'\x17\x14\x11\x12'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
