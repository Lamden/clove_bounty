
from clove.network.bitcoin import Bitcoin


class Bitradio(Bitcoin):
    """
    Class with all the necessary BRO network information based on
    http://www.github.com/thebitradio/Bitradio/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'bitradio'
    symbols = ('BRO', )
    seeds = ('node1.bitrad.io', 'node2.bitrad.io', 'node3.bitrad.io')
    port = 32454
    message_start = b'\xd3\x1a\x3d\xe4'
    base58_prefixes = {
        'PUBKEY_ADDR': 26,
        'SCRIPT_ADDR': 102,
        'SECRET_KEY': 128
    }


class BitradioTestNet(Bitradio):
    """
    Class with all the necessary BRO testing network information based on
    http://www.github.com/thebitradio/Bitradio/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-bitradio'
    seeds = ()
    port = 58870
    message_start = b'\x2f\xca\x4d\x3e'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 137,
        'SECRET_KEY': 161
    }
