from clove.network.bitcoin import Bitcoin


class Vsync(Bitcoin):
    """
    Class with all the necessary Vsync (VSX) network information based on
    https://github.com/VsyncCrypto/VSX/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'vsync'
    symbols = ('VSX', )
    seeds = ('vsyncseed.vsync.pw', 'node.vsync.pw', 'node1.vsync.pw', 'node2.vsync.pw', 'node3.vsync.pw',
             'node4.vsync.pw', 'node5.vsync.pw', 'node6.vsync.pw')
    port = 65010
    message_start = b'\x21\x55\x0a\x5a'
    base58_prefixes = {
        'PUBKEY_ADDR': 70,
        'SCRIPT_ADDR': 13,
        'SECRET_KEY': 212
    }


class VsyncTestNet(Vsync):
    """
    Class with all the necessary Vsync (VSX) testing network information based on
    https://github.com/VsyncCrypto/VSX/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-vsync'
    seeds = ('vsync-testnet.seed.fuzzbawls.pw',
             'vsync-testnet.seed2.fuzzbawls.pw', 's3v3nh4cks.ddns.net')
    port = 51474
    message_start = b'\x45\x76\x65\xba'
    base58_prefixes = {
        'PUBKEY_ADDR': 139,
        'SCRIPT_ADDR': 19,
        'SECRET_KEY': 239
    }
