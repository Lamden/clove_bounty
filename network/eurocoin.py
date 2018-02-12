
from clove.network.bitcoin import Bitcoin


class Eurocoin(Bitcoin):
    """
    Class with all the necessary EUC network information based on
    http://www.github.com/scriptexpert/Eurocoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'eurocoin'
    symbols = ('EUC', )
    seeds = ('seed.viapool.tk', 'seed1.eurocoin-euc.com', 'seed2.eurocoin-euc.com', 'seed3.eurocoin-euc.com')
    port = 11775


class EurocoinTestNet(Eurocoin):
    """
    Class with all the necessary EUC testing network information based on
    http://www.github.com/scriptexpert/Eurocoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-eurocoin'
    seeds = ('seed.viapool.tk',)
    port = 11775
