
from clove.network.bitcoin import Bitcoin


class Xonecoin(Bitcoin):
    """
    Class with all the necessary XOC network information based on
    https://github.com/xonecoin/xonecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'xonecoin'
    symbols = ('XOC', )
    nodes = ('52.42.45.57', )
    port = 55448
    message_start = b'\xf3\x2d\xa5\x71'
    base58_prefixes = {
        'PUBKEY_ADDR': 45,
        'SCRIPT_ADDR': 142,
        'SECRET_KEY': 173
    }


class XonecoinTestNet(Xonecoin):
    """
    Class with all the necessary XOC testing network information based on
    https://github.com/xonecoin/xonecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-xonecoin'
    seeds = ()
    port = 55447
