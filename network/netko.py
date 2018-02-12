
from clove.network.bitcoin import Bitcoin


class Netko(Bitcoin):
    """
    Class with all the necessary NETKO network information based on
    http://www.github.com/netkotech/netko/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'netko'
    symbols = ('NETKO', )
    seeds = ('node1.netko.tech', 'node2.netko.tech', 'node3.netko.tech', 'node4.netko.tech')
    port = 25960


class NetkoTestNet(Netko):
    """
    Class with all the necessary NETKO testing network information based on
    http://www.github.com/netkotech/netko/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-netko'
    seeds = ()
    port = 25961
