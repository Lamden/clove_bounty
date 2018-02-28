
from clove.network.bitcoin import Bitcoin


class Unify(Bitcoin):
    """
    Class with all the necessary UNIFY network information based on
    http://www.github.com/SBDomains/unify-source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'unify'
    symbols = ('UNIFY', )
    seeds = ('95.85.59.180', '145.239.89.215', '158.69.212.99', 'node1.unifycoin.ovh', 'node2.unifycoin.ovh',
             'node3.unifycoin.ovh', 'node1.unifycoin.pl', 'node2.unifycoin.pl', 'node3.unifycoin.pl')
    port = 18649


class UnifyTestNet(Unify):
    """
    Class with all the necessary UNIFY testing network information based on
    http://www.github.com/SBDomains/unify-source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-unify'
    seeds = ()
    port = 28649
