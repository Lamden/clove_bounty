
from clove.network.bitcoin import Bitcoin


class MindCoin(Bitcoin):
    """
    Class with all the necessary MND network information based on
    http://www.github.com/MindCoinTeam/MindCoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'mindcoin'
    symbols = ('MND', )
    seeds = ('node1.mindcoin.xyz', 'node2.mindcoin.xyz', 'node3.mindcoin.xyz', 'mnd.blockpioneers.info')
    port = 34281


class MindCoinTestNet(MindCoin):
    """
    Class with all the necessary MND testing network information based on
    http://www.github.com/MindCoinTeam/MindCoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-mindcoin'
    seeds = ()
    port = 34291
