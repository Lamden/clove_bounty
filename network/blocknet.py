from clove.network.bitcoin import Bitcoin


class Blocknet(Bitcoin):
    """
    Class with all the necessary Blocknet (BLOCK) network information based on
    https://github.com/BlocknetDX/BlockDX/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'blocknet'
    symbols = ('BLOCK', )
    seeds = ('178.62.90.213', '138.197.73.214', '34.235.49.248')
    port = 41412


class BlocknetTestNet(Blocknet):
    """
    Class with all the necessary Blocknet (BLOCK) testing network information based on
    https://github.com/BlocknetDX/BlockDX/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-blocknet'
    seeds = ('178.62.90.213', '138.197.73.214', '34.235.49.248')
    port = 41474
