
from clove.network.bitcoin import Bitcoin


class Innova(Bitcoin):
    """
    Class with all the necessary INN network information based on
    http://www.github.com/innovacoin/innova/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'innova'
    symbols = ('INN', )
    seeds = ('dnss1.innovacoin.info', 'dnss2.innovacoin.info')
    port = 14520


class InnovaTestNet(Innova):
    """
    Class with all the necessary INN testing network information based on
    http://www.github.com/innovacoin/innova/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-innova'
    seeds = ()
    port = 15520
