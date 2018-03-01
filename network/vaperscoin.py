
from clove.network.bitcoin import Bitcoin


class VapersCoin(Bitcoin):
    """
    Class with all the necessary VPRC network information based on
    http://www.github.com/vaperscoin/vaperscoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'vaperscoin'
    symbols = ('VPRC', )
    seeds = ('37.187.125.97',)
    port = 4444


class VapersCoinTestNet(VapersCoin):
    """
    Class with all the necessary VPRC testing network information based on
    http://www.github.com/vaperscoin/vaperscoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-vaperscoin'
    seeds = ('seed.mophides.com', 'seed.dglibrary.org', 'seed.epcchain.info',
             'testepc-seed.lionservers.de', 'testepc-seed-static.lionservers.de')
    port = 14444
