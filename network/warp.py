
from clove.network.bitcoin import Bitcoin


class Warp(Bitcoin):
    """
    Class with all the necessary WARP network information based on
    https://github.com/shapetwist/warp/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'warp'
    symbols = ('WARP', )
    nodes = ('84.200.4.70', )
    port = 31312
    message_start = b'\x5a\xc3\x82\xd3'
    base58_prefixes = {
        'PUBKEY_ADDR': 73,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 201
    }


class WarpTestNet(Warp):
    """
    Class with all the necessary WARP testing network information based on
    https://github.com/shapetwist/warp/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-warp'
    seeds = ()
    port = 31313
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
