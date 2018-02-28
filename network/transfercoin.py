
from clove.network.bitcoin import Bitcoin


class TransferCoin(Bitcoin):
    """
    Class with all the necessary TX network information based on
    http://www.github.com/transferdev/Transfercoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'transfercoin'
    symbols = ('TX', )
    seeds = ('txdns.infernopool.com', 'txdns2.infernopool.com',
             'txdns3.infernopool.com')
    port = 17170


class TransferCoinTestNet(TransferCoin):
    """
    Class with all the necessary TX testing network information based on
    http://www.github.com/transferdev/Transfercoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-transfercoin'
    seeds = ()
    port = 27170
