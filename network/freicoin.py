from clove.network.bitcoin import Bitcoin


class Freicoin(Bitcoin):
    """
    Class with all the necessary Freicoin (FRC) network information based on
    https://github.com/freicoin/freicoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'freicoin'
    symbols = ('FRC', )
    seeds = ('seed.freico.in', 'fledge.freico.in', 'seed.mainnet.freicoin.pw', 'dnsseed.sicanet.net')
    port = 8639


class FreicoinTestNet(Freicoin):
    """
    Class with all the necessary Freicoin (FRC) testing network information based on
    https://github.com/freicoin/freicoin/blob/master/src/net.cpp    
    (date of access: 02/17/2018)
    """
    name = 'test-freicoin'
    seeds = ('seed.testnet.freicoin.pw')
    port = 18639
