
from clove.network.bitcoin import Bitcoin


class Opescoin(Bitcoin):
    """
    Class with all the necessary OPES network information based on
    http://www.github.com/OpesCoin/OPES/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'opescoin'
    symbols = ('OPES', )
    nodes = ('104.218.50.15', )
    port = 6222
    message_start = b'\xf3\xf1\xd2\xb5'
    base58_prefixes = {
        'PUBKEY_ADDR': 115,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 243
    }


class OpescoinTestNet(Opescoin):
    """
    Class with all the necessary OPES testing network information based on
    http://www.github.com/OpesCoin/OPES/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-opescoin'
    seeds = ('dnsseed.OPES.org', )
    port = 26222
    message_start = b'\xa1\xb2\xd1\xf8'
    base58_prefixes = {
        'PUBKEY_ADDR': 112,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 240
    }
