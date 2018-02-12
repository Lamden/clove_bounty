
from clove.network.bitcoin import Bitcoin


class Myriad(Bitcoin):
    """
    Class with all the necessary XMY network information based on
    http://www.github.com/myriadteam/myriadcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'myriad'
    symbols = ('XMY', )
    seeds = ('seed1.myriadcoin.org', 'seed2.myriadcoin.org', 'seed3.myriadcoin.org', 'seed4.myriadcoin.org', 'seed5.myriadcoin.org', 'seed6.myriadcoin.org', 'seed7.myriadcoin.org', 'seed8.myriadcoin.org', 'myriadseed1.cryptap.us')
    port = 10888


class MyriadTestNet(Myriad):
    """
    Class with all the necessary XMY testing network information based on
    http://www.github.com/myriadteam/myriadcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-myriad'
    seeds = ('testseed1.myriadcoin.org', 'myriadtestseed1.cryptap.us')
    port = 20888
