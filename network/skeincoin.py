
from clove.network.bitcoin import Bitcoin


class Skeincoin(Bitcoin):
    """
    Class with all the necessary SKC network information based on
    http://www.github.com/skeincoin/skeincoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'skeincoin'
    symbols = ('SKC', )
    seeds = ('seed-a.skeincoin.net', 'seed-b.skeincoin.net', 'seed-c.skeincoin.net', 'seed-d.skeincoin.net', 'seed-e.skeincoin.net', 'seed-f.skeincoin.net', 'seed-g.skeincoin.net', 'seed-h.skeincoin.net', 'skein1.ignorelist.com', 'skein2.ignorelist.com', 'skein3.ignorelist.com')
    port = 11230


class SkeincoinTestNet(Skeincoin):
    """
    Class with all the necessary SKC testing network information based on
    http://www.github.com/skeincoin/skeincoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-skeincoin'
    seeds = ()
    port = 27711
