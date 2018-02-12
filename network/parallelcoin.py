
from clove.network.bitcoin import Bitcoin


class ParallelCoin(Bitcoin):
    """
    Class with all the necessary DUO network information based on
    http://www.github.com/marcetin/parallelcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'parallelcoin'
    symbols = ('DUO', )
    seeds = ('seed1.parallelcoin.info', 'seed3.parallelcoin.info', 'seed2.parallelcoin.info', 'seed4.parallelcoin.info', 'seed5.parallelcoin.info')
    port = 11047


class ParallelCoinTestNet(ParallelCoin):
    """
    Class with all the necessary DUO testing network information based on
    http://www.github.com/marcetin/parallelcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-parallelcoin'
    seeds = ('seed2.parallelcoin.info',)
    port = 21047
