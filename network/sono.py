
from clove.network.bitcoin import Bitcoin


class SONO(Bitcoin):
    """
    Class with all the necessary ALTCOM network information based on
    http://www.github.com/altcommunitycoin/altcommunitycoin-skunk/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'sono'
    symbols = ('ALTCOM', )
    seeds = ('109.230.231.216', '109.230.231.221', '212.109.218.47', 'zPools.de')
    port = 29855


class SONOTestNet(SONO):
    """
    Class with all the necessary ALTCOM testing network information based on
    http://www.github.com/altcommunitycoin/altcommunitycoin-skunk/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-sono'
    seeds = ('',)
    port = 29844
