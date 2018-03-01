
from clove.network.bitcoin import Bitcoin


class Vivo(Bitcoin):
    """
    Class with all the necessary VIVO network information based on
    http://www.github.com/vivocoin/vivo/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'vivo'
    symbols = ('VIVO', )
    seeds = ('vivoseed1.vivoseeds.win',)
    port = 12845
    message_start = b'\x1d\x42\x5b\xa7'
    base58_prefixes = {
        'PUBKEY_ADDR': 70,
        'SCRIPT_ADDR': 10,
        'SECRET_KEY': 198
    }


class VivoTestNet(Vivo):
    """
    Class with all the necessary VIVO testing network information based on
    http://www.github.com/vivocoin/vivo/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-vivo'
    seeds = ('testnet-dns.vivonodes.space',)
    port = 13845
    message_start = b'\xd1\x24\xb5\x7a'
    base58_prefixes = {
        'PUBKEY_ADDR': 112,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 240
    }
