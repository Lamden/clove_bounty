from clove.network.bitcoin import Bitcoin


class Flappycoin(Bitcoin):
    """
    Class with all the necessary Flappycoin (FLAP) network information based on
    https://github.com/flappycoin-project/flappycoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'flappycoin'
    symbols = ('FLAP', )
    seeds = ('seed.terracoin.io', 'dnsseed.flap.so')
    port = 11556


class FlappycoinTestNet(Flappycoin):
    """
    Class with all the necessary Flappycoin (FLAP) testing network information based on
    https://github.com/flappycoin-project/flappycoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-flappycoin'
    seeds = ('dnsseed.flap.so', )
    port = 33556
