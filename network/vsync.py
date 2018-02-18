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


class VsyncTestNet(Vsync):
    """
    Class with all the necessary Vsync (VSX) testing network information based on
    https://github.com/VsyncCrypto/VSX/blob/master/src/chainparams.cpp    
    (date of access: 02/17/2018)
    """
    name = 'test-vsync'
    seeds = ('vsync-testnet.seed.fuzzbawls.pw', 'vsync-testnet.seed2.fuzzbawls.pw', 's3v3nh4cks.ddns.net', '88.198.192.110')
    port = 51474
