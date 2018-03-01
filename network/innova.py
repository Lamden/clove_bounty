
from clove.network.bitcoin import Bitcoin


class Innova(Bitcoin):
    """
    Class with all the necessary INN network information based on
    http://www.github.com/innovacoin/innova/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'innova'
    symbols = ('INN', )
    seeds = ('dnss1.innovacoin.info', 'dnss2.innovacoin.info')
    port = 14520
    message_start = b'\x3c\x2a\x3a\xb9'
    base58_prefixes = {
        'PUBKEY_ADDR': 102,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 195
    }


class InnovaTestNet(Innova):
    """
    Class with all the necessary INN testing network information based on
    http://www.github.com/innovacoin/innova/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-innova'
    seeds = ()
    port = 15520
    message_start = b'\xb1\xa4\xd5\x7c'
    base58_prefixes = {
        'PUBKEY_ADDR': 112,
        'SCRIPT_ADDR': 10,
        'SECRET_KEY': 240
    }
