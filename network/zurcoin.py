
from clove.network.bitcoin import Bitcoin


class Zurcoin(Bitcoin):
    """
    Class with all the necessary ZUR network information based on
    http://www.github.com/zurcoin/zurcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'zurcoin'
    symbols = ('ZUR', )
    seeds = ('50.116.55.60',)
    port = 18071
    message_start = b'\xfe\xa5\x03\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 69,
        'SCRIPT_ADDR': 9,
        'SECRET_KEY': 197
    }


class ZurcoinTestNet(Zurcoin):
    """
    Class with all the necessary ZUR testing network information based on
    http://www.github.com/zurcoin/zurcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-zurcoin'
    seeds = ()
    port = 21973
    message_start = b'\x01\x1a\x39\xf7'
    base58_prefixes = {
        'PUBKEY_ADDR': 119,
        'SCRIPT_ADDR': 199,
        'SECRET_KEY': 247
    }
