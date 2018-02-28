from clove.network.bitcoin import Bitcoin


class SegWit2X(Bitcoin):
    """
    Class with all the necessary SegWit2X (B2X) network information based on
    https://github.com/SegwitB2X/bitcoin2x/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'segwit2x'
    symbols = ('B2X', )
    seeds = ('node1.b2x-segwit.io',
             'node2.b2x-segwit.io', 'node3.b2x-segwit.io')
    port = 8333


class SegWit2XTestNet(SegWit2X):
    """
    Class with all the necessary SegWit2X (B2X) testing network information based on
    https://github.com/SegwitB2X/bitcoin2x/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-segwit2x'
    seeds = ('node1.b2x-segwit.io',
             'node2.b2x-segwit.io', 'node3.b2x-segwit.io')
    port = 18333
