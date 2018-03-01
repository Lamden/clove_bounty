
from clove.network.bitcoin import Bitcoin


class VectorAI(Bitcoin):
    """
    Class with all the necessary VEC2 network information based on
    http://www.github.com/vectorcoindev/Vector/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'vectorai'
    symbols = ('VEC2', )
    seeds = ('104.207.128.39', '45.32.234.225')
    port = 1715
    message_start = b'\xe7\x92\x60\xe8'
    base58_prefixes = {
        'PUBKEY_ADDR': 70,
        'SCRIPT_ADDR': 45,
        'SECRET_KEY': 186
    }


class VectorAITestNet(VectorAI):
    """
    Class with all the necessary VEC2 testing network information based on
    http://www.github.com/vectorcoindev/Vector/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-vectorai'
    seeds = ()
    port = 11715
    message_start = b'\x20\x3B\xEA\x59'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 146,
        'SECRET_KEY': 211
    }
