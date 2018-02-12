
from clove.network.bitcoin import Bitcoin


class Coin(Bitcoin):
    """
    Class with all the necessary SIB network information based on
    http://www.github.com/ivansib/sibcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'coin'
    symbols = ('SIB', )
    seeds = ('dnsseed.sibcoin.net', 'dnsseed.chervonec.info', 'dnsseed1.darknode.ru', 'dnsseed2.darknode.ru', 'dnsseed3.darknode.ru')
    port = 1945


class CoinTestNet(Coin):
    """
    Class with all the necessary SIB testing network information based on
    http://www.github.com/ivansib/sibcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-coin'
    seeds = ('testnet-seed.dashdot.io', 'test.dnsseed.masternode.io')
    port = 11945
