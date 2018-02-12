from clove.network.bitcoin import Bitcoin


class Zencash(Bitcoin):
    """
    Class with all the necessary ZenCash (ZEN) network information based on
    https://github.com/ZencashOfficial/zen/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'zencash'
    symbols = ('ZEN', )
    seeds = ('dnsseed.zensystem.io', 'dnsseed.zenseed.network', 'zpool.blockoperations.com', 'node1.zenchain.info', 'mainnet.zenseed.network', 'mainnet.zensystem.io')
    port = 9033


class ZencashTestNet(Zencash):
    """
    Class with all the necessary ZenCash (ZEN) testing network information based on
    https://github.com/ZencashOfficial/zen/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-zencash'
    seeds = ('dnsseed.testnet.zensystem.io', 'zpool2.blockoperations.com', 'node.scottrockcafe.com', 'testnet.zensystem.io')
    port = 19033
