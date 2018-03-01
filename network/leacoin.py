
from clove.network.bitcoin import Bitcoin


class LeaCoin(Bitcoin):
    """
    Class with all the necessary LEA network information based on
    http://www.github.com/leacoin/LeaCoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'leacoin'
    symbols = ('LEA', )
    seeds = ('dnsseed.leacoin.org',)
    port = 18123
    message_start = b'\x12\x0c\x07\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 30,
        'SECRET_KEY': 224
    }


class LeaCoinTestNet(LeaCoin):
    """
    Class with all the necessary LEA testing network information based on
    http://www.github.com/leacoin/LeaCoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-leacoin'
    seeds = ('test.leacoin.org',)
    port = 55534
    message_start = b'\x01\xfe\xfe\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 130,
        'SCRIPT_ADDR': 30,
        'SECRET_KEY': 239
    }
