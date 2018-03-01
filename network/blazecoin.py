
from clove.network.bitcoin import Bitcoin


class BlazeCoin(Bitcoin):
    """
    Class with all the necessary BLZ network information based on
    http://www.github.com/wpstudio/blazecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'blazecoin'
    symbols = ('BLZ', )
    seeds = ('172.245.137.35',)
    port = 55414
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 26,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 154
    }


class BlazeCoinTestNet(BlazeCoin):
    """
    Class with all the necessary BLZ testing network information based on
    http://www.github.com/wpstudio/blazecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-blazecoin'
    seeds = ('testnet.seedtest.blazeco.in',)
    port = 75414
    message_start = b'\xed\xb2\xa8\xcd'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
