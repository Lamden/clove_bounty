
from clove.network.bitcoin import Bitcoin


class Zurcoin(Bitcoin):
    """
    Class with all the necessary ZUR network information based on
    http://www.github.com/zurcoin/zurcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'zurcoin'
    symbols = ('ZUR', )
    nodes = ('50.116.55.60', )
    port = 18071
    message_start = b'\xfe\xa5\x03\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 69,
        'SCRIPT_ADDR': 9,
        'SECRET_KEY': 197
    }
