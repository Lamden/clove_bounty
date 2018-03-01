
from clove.network.bitcoin import Bitcoin


class Rubycoin(Bitcoin):
    """
    Class with all the necessary RBY network information based on
    http://www.github.com/rubycoinorg/rubycoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'rubycoin'
    symbols = ('RBY', )
    seeds = ('neptune.rubycoin.org', 'pluto.rubycoin.org', )
    port = 5937
    message_start = b'\x13\x12\x16\x11'
    base58_prefixes = {
        'PUBKEY_ADDR': 60,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 188
    }


class RubycoinTestNet(Rubycoin):
    """
    Class with all the necessary RBY testing network information based on
    http://www.github.com/rubycoinorg/rubycoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-rubycoin'
    seeds = ()
    port = 55937
    message_start = b'\x17\x14\x11\x12'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
