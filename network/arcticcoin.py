
from clove.network.bitcoin import Bitcoin


class ArcticCoin(Bitcoin):
    """
    Class with all the necessary ARC network information based on
    http://www.github.com/ArcticCore/arcticcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'arcticcoin'
    symbols = ('ARC', )
    nodes = ('5.9.65.168', '5.9.55.201', '78.46.75.49', '78.47.238.36', )
    port = 7209
    message_start = b'\x3d\xd2\x28\x61'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 176
    }


class ArcticCoinTestNet(ArcticCoin):
    """
    Class with all the necessary ARC testing network information based on
    http://www.github.com/ArcticCore/arcticcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-arcticcoin'
    nodes = ('5.9.65.168', '5.9.55.201', '78.46.75.49', '78.47.238.36', )
    port = 17209
    message_start = b'\x2a\x2c\x2c\x2d'
    base58_prefixes = {
        'PUBKEY_ADDR': 83,
        'SCRIPT_ADDR': 9,
        'SECRET_KEY': 239
    }
