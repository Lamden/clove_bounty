
from clove.network.bitcoin import Bitcoin


class LEOcoin(Bitcoin):
    """
    Class with all the necessary LEO network information based on
    http://www.github.com/Leocoin-project/LEOcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'leocoin'
    symbols = ('LEO', )
    seeds = ('dnsseed.leocoin.org', 'leoseed.leocoin.org', 'node1.leocoin.org', 'node2.leocoin.org', 'node3.leocoin.org', 'node4.leocoin.org', 'node5.leocoin.org', 'node6.leocoin.org', 'node7.leocoin.org', 'node8.leocoin.org', 'node9.leocoin.org', 'node10.leocoin.org')
    port = 5840


class LEOcoinTestNet(LEOcoin):
    """
    Class with all the necessary LEO testing network information based on
    http://www.github.com/Leocoin-project/LEOcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-leocoin'
    seeds = ()
    port = 15840
