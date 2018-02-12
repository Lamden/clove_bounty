
from clove.network.bitcoin import Bitcoin


class Acoin(Bitcoin):
    """
    Class with all the necessary ACOIN network information based on
    http://www.github.com/acoin-project/acoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'acoin'
    symbols = ('ACOIN', )
    seeds = ('seed1.a-coin.info', 'seed2.a-coin.info', 'seed3.a-coin.info', 'seed4.a-coin.info', 'seed5.a-coin.info', 'seed6.a-coin.info', 'seed7.a-coin.info', 'seed8.a-coin.info')
    port = 17883


class AcoinTestNet(Acoin):
    """
    Class with all the necessary ACOIN testing network information based on
    http://www.github.com/acoin-project/acoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-acoin'
    seeds = ()
    port = 27883
