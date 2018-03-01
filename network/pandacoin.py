
from clove.network.bitcoin import Bitcoin


class Pandacoin(Bitcoin):
    """
    Class with all the necessary PND network information based on
    http://www.github.com/DigitalPandacoin/pandacoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'pandacoin'
    symbols = ('PND', )
    seeds = ('server1.cryptodepot.org',)
    port = 22445
    message_start = b'\xc0\xc0\xc0\xc0'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 22,
        'SECRET_KEY': 183
    }


class PandacoinTestNet(Pandacoin):
    """
    Class with all the necessary PND testing network information based on
    http://www.github.com/DigitalPandacoin/pandacoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-pandacoin'
    seeds = ('pndstats.com',)
    port = 44656
    message_start = b'\xfc\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 113,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 241
    }
