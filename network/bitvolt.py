
from clove.network.bitcoin import Bitcoin


class Bitvolt(Bitcoin):
    """
    Class with all the necessary VOLT network information based on
    http://www.github.com/voltcoin/Volt/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'bitvolt'
    symbols = ('VOLT', )
    nodes = ('198.211.126.38', )
    port = 11516
    message_start = b'\x12\x69\x51\x22'
    base58_prefixes = {
        'PUBKEY_ADDR': 70,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 166
    }


class BitvoltTestNet(Bitvolt):
    """
    Class with all the necessary VOLT testing network information based on
    http://www.github.com/voltcoin/Volt/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-bitvolt'
    seeds = ()
    port = 25723
    message_start = b'\x12\x0b\x1e\xbc'
    base58_prefixes = {
        'PUBKEY_ADDR': 113,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 241
    }
