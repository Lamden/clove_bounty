
from clove.network.bitcoin import Bitcoin


class Rubycoin(Bitcoin):
    """
    Class with all the necessary RBY network information based on
    http://www.github.com/rubycoinorg/rubycoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'rubycoin'
    symbols = ('RBY', )
    seeds = ('neptune.rubycoin.org', 'pluto.rubycoin.org')
    port = 5937


class RubycoinTestNet(Rubycoin):
    """
    Class with all the necessary RBY testing network information based on
    http://www.github.com/rubycoinorg/rubycoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-rubycoin'
    seeds = ()
    port = 55937
