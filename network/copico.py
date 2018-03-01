
from clove.network.bitcoin import Bitcoin


class Copico(Bitcoin):
    """
    Class with all the necessary XCPO network information based on
    http://www.github.com/copicogithub1/copico/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'copico'
    symbols = ('XCPO', )
    seeds = ('seed1.copico.io', 'seed2.copico.io', )
    port = 17356
    message_start = b'\x4d\xb1\x24\xc1'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 43,
        'SECRET_KEY': 144
    }


class CopicoTestNet(Copico):
    """
    Class with all the necessary XCPO testing network information based on
    http://www.github.com/copicogithub1/copico/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-copico'
    seeds = ()
    port = 17357
    message_start = b'\x21\x7c\xb4\xba'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 43,
        'SECRET_KEY': 229
    }
