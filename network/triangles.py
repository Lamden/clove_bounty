from clove.network.bitcoin import Bitcoin


class Triangles(Bitcoin):
    """
    Class with all the necessary Triangles network information based on
    https://github.com/TrianglesProject/triangles/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'triangles'
    symbols = ('TRI', )
    seeds = ("dnsseed.bit.diamonds", )
    port = 17771
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 193
    }


class DiamondTestNet(Triangles):
    """
    Class with all the necessary Diamond testing network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-diamond'
    seeds = ("dnsseed.bit.diamonds", )
    port = 51474
    message_start = b'\x45\x76\x65\xba'
    base58_prefixes = {
        'PUBKEY_ADDR': 139,
        'SCRIPT_ADDR': 19,
        'SECRET_KEY': 239
    }
