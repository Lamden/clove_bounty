
from clove.network.bitcoin import Bitcoin


class Flaxscript(Bitcoin):
    """
    Class with all the necessary FLAX network information based on
    http://www.github.com/thegreatoldone/flaxscript/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'flaxscript'
    symbols = ('FLAX', )
    nodes = ('192.99.37.133', '84.200.4.67', '213.32.98.226', )
    port = 17235
    message_start = b'\x01\x07\x02\x03'
    base58_prefixes = {
        'PUBKEY_ADDR': 43,
        'SCRIPT_ADDR': 4,
        'SECRET_KEY': 156
    }


class FlaxscriptTestNet(Flaxscript):
    """
    Class with all the necessary FLAX testing network information based on
    http://www.github.com/thegreatoldone/flaxscript/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-flaxscript'
    seeds = ('', )
    port = 23990
    message_start = b'\xfb\xc2\x11\x02'
    base58_prefixes = {
        'PUBKEY_ADDR': 105,
        'SCRIPT_ADDR': 44,
        'SECRET_KEY': 216
    }
