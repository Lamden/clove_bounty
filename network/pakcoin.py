
from clove.network.bitcoin import Bitcoin


class Pakcoin(Bitcoin):
    """
    Class with all the necessary PAK network information based on
    http://www.github.com/pakcoin-project/pakcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'pakcoin'
    symbols = ('PAK', )
    seeds = ('seed.pakcoin.org', )
    port = 7867
    message_start = b'\x70\x61\x6b\x63'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 183
    }


class PakcoinTestNet(Pakcoin):
    """
    Class with all the necessary PAK testing network information based on
    http://www.github.com/pakcoin-project/pakcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-pakcoin'
    seeds = ()
    port = 17867
    message_start = b'\xfc\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
