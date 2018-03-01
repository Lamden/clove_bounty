
from clove.network.bitcoin import Bitcoin


class CBit(Bitcoin):
    """
    Class with all the necessary XCT network information based on
    http://www.github.com/Infernoman/C-Bit/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'c-bit'
    symbols = ('XCT', )
    seeds = ('192.241.191.47',)
    port = 8289
    message_start = b'\xde\xad\xfe\xd5'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


class CBitTestNet(CBit):
    """
    Class with all the necessary XCT testing network information based on
    http://www.github.com/Infernoman/C-Bit/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-c-bit'
    seeds = ('159.203.31.151', '192.241.179.42')
    port = 18289
    message_start = b'\x0b\x10\xd9\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
