from clove.network.bitcoin import Bitcoin


class Magi(Bitcoin):
    """
    Class with all the necessary Magi (XMG) network information based on
    https://github.com/magi-project/magi/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'magi'
    symbols = ('XMG', )
    seeds = ('seed.m-core.org', 'seed.m-chain.info',
             'seed.magi.filoozom.com', 'seed.systms.org')
    port = 8233


class MagiTestNet(Magi):
    """
    Class with all the necessary Magi (XMG) testing network information based on
    https://github.com/magi-project/magi/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-magi'
    seeds = ('test-seed.m-core.org', 'test-seed.m-chain.info',
             'test-seed.magi.filoozom.com', 'test-seed.systms.org')
    port = 18233
