from clove.network.bitcoin import Bitcoin


class BlakeStar(Bitcoin):
    """
    Class with all the necessary BlakeStar network information based on
    https://github.com/Blakestarcoin/BLASS/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'blakestar'
    symbols = ('BLAS', )
    nodes = ("213.169.33.11", )
    port = 14442
    message_start = b'\xea\x11\x7a\xcc'
    base58_prefixes = {
        'PUBKEY_ADDR': 26,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 154
    }


class BlakeStarTestNet(BlakeStar):
    """
    Class with all the necessary BlakeStar testing network information based on
    https://github.com/Blakestarcoin/BLASS/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-blakestar'
    seeds = ("test1.BlakeStar.pw", )
    port = 24442
    message_start = b'\xa7\x41\xae\x7c'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
