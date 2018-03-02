
from clove.network.bitcoin import Bitcoin


class Hyper(Bitcoin):
    """
    Class with all the necessary HYPER network information based on
    http://www.github.com/CryptoDatabase/hyper/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'hyper'
    symbols = ('HYPER', )
    nodes = ('195.74.52.227', )
    port = 11194
    message_start = b'\xce\xfb\xfa\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 100,
        'SCRIPT_ADDR': 101,
        'SECRET_KEY': 104
    }


class HyperTestNet(Hyper):
    """
    Class with all the necessary HYPER testing network information based on
    http://www.github.com/CryptoDatabase/hyper/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-hyper'
    seeds = ()
    port = 11199
    message_start = b'\xcd\xf1\xc0\xef'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
