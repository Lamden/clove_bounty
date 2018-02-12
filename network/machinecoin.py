
from clove.network.bitcoin import Bitcoin


class Machinecoin(Bitcoin):
    """
    Class with all the necessary MAC network information based on
    http://www.github.com/machinecoin-project/machinecoin-core/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'machinecoin'
    symbols = ('MAC', )
    seeds = ('dnsseed1.machinecoin.org',)
    port = 40333


class MachinecoinTestNet(Machinecoin):
    """
    Class with all the necessary MAC testing network information based on
    http://www.github.com/machinecoin-project/machinecoin-core/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-machinecoin'
    seeds = ('dnsseed2.machinecoin.org', 'testnetdnsseed1.machinecoin.org', 'testnetdnsseed2.machinecoin.org')
    port = 50333
