
from clove.network.bitcoin import Bitcoin


class Bubble(Bitcoin):
    """
    Class with all the necessary BUB network information based on
    http://www.github.com/spayse/Bubble/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'bubble'
    symbols = ('BUB', )
    seeds = ('194.135.85.45',)
    port = 15716
    message_start = b'\xcd\x21\x19\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 53,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


class BubbleTestNet(Bubble):
    """
    Class with all the necessary BUB testing network information based on
    http://www.github.com/spayse/Bubble/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-bubble'
    seeds = ()
    port = 38881
    message_start = b'\x08\x12\x16\x19'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
