
from clove.network.bitcoin import Bitcoin


class AquariusCoin(Bitcoin):
    """
    Class with all the necessary ARCO network information based on
    http://www.github.com/AquariusNetwork/ARCO/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'aquariuscoin'
    symbols = ('ARCO', )
    seeds = ('node1.aquariuscoin.com', 'node2.aquariuscoin.com', 'node3.aquariuscoin.com', 'node4.aquariuscoin.com', 'node5.aquariuscoin.com', 'node6.aquariuscoin.com', 'node7.aquariuscoin.com', 'node8.aquariuscoin.com', 'node9.aquariuscoin.com', 'node.bit-coin.pw')
    port = 6205


class AquariusCoinTestNet(AquariusCoin):
    """
    Class with all the necessary ARCO testing network information based on
    http://www.github.com/AquariusNetwork/ARCO/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-aquariuscoin'
    seeds = ()
    port = 16205
