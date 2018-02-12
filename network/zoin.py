
from clove.network.bitcoin import Bitcoin


class Zoin(Bitcoin):
    """
    Class with all the necessary ZOI network information based on
    http://www.github.com/zoinofficial/zoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'zoin'
    symbols = ('ZOI', )
    seeds = ('node11.zoinofficial.com', 'node1.zoinofficial.com', 'node2.zoinofficial.com', 'node3.zoinofficial.com', 'node4.zoinofficial.com')
    port = 8255


class ZoinTestNet(Zoin):
    """
    Class with all the necessary ZOI testing network information based on
    http://www.github.com/zoinofficial/zoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-zoin'
    seeds = ('node5.zoinofficial.com', 'node1.zoinofficial.com', 'node2.zoinofficial.com', 'node3.zoinofficial.com', 'node4.zoinofficial.com', 'node5.zoinofficial.com', 'node6.zoinofficial.com', 'node7.zoinofficial.com', 'node8.zoinofficial.com', 'node9.zoinofficial.com', 'node10.zoinofficial.com', '92.247.116.44', '92.247.116.44', 'seed.tbtc.petertodd.org', 'testnet-seed.bluematt.me', 'testnet-seed.bitcoin.schildbach.de')
    port = 28168
