from clove.network.bitcoin import Bitcoin


class Quark(Bitcoin):
    """
    Class with all the necessary Quark (QRK) network information based on
    https://github.com/quark-project/quark/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'quark'
    symbols = ('QRK', )
    seeds = ('seed1.qrknet.info', 'seed2.qrknet.info', 'seed3.qrknet.info', 'seed4.qrknet.info',
			 'seed5.qrknet.info', 'seed6.qrknet.info', 'seed7.qrknet.info', 'seed8.qrknet.info')
    port = 11973


class QuarkTestNet(Quark):
    """
    Class with all the necessary Quark (QRK) testing network information based on
    https://github.com/quark-project/quark/blob/master/src/chainparams.cpp    
    (date of access: 02/16/2018)
    """
    name = 'test-quark'
    seeds = ('testseed1.qrknet.info')
    port = 21973
