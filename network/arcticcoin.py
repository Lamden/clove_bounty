
from clove.network.bitcoin import Bitcoin


class ArcticCoin(Bitcoin):
    """
    Class with all the necessary ARC network information based on
    http://www.github.com/ArcticCore/arcticcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'arcticcoin'
    symbols = ('ARC', )
    seeds = ('5.9.65.168', '5.9.55.201', '78.46.75.49', '78.47.238.36')
    port = 7209


class ArcticCoinTestNet(ArcticCoin):
    """
    Class with all the necessary ARC testing network information based on
    http://www.github.com/ArcticCore/arcticcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-arcticcoin'
    seeds = ('5.9.65.168', '5.9.55.201', '78.46.75.49', '78.47.238.36')
    port = 17209
