from clove.network.bitcoin import Bitcoin


class Sarcoin(Bitcoin):
    """
    Class with all the necessary Sarcoin network information based on
    https://github.com/sarcoin/SARCoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'sarcoin'
    symbols = ('SAR', )
    seeds = ("explorer.sarcoin.info",
             "node1.sarcoin.info",
             "node2.sarcoin.info",
             "node3.sarcoin.info",
             "node4.sarcoin.info",
             "node5.sarcoin.info",
             "node6.sarcoin.info",
             "node7.sarcoin.info",
             "node8.sarcoin.info")
    port = 25902
	
