from clove.network.bitcoin import Bitcoin


class MindCoin(Bitcoin):
    """
    Class with all the necessary MindCoin network information based on
    https://github.com/mindcointeam/mindcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'mindcoin'
    symbols = ('MND', )
    seeds = ("node1.mindcoin.xyz",
             "node2.mindcoin.xyz",
             "node3.mindcoin.xyz",
             "mnd.blockpioneers.info")
    port = 34281


# Has no testnet

