
from clove.network.bitcoin import Bitcoin


class Elite(Bitcoin):
    """
    Class with all the necessary 1337 network information based on
    https://github.com/xenonflux/1337/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'elite'
    symbols = ('1337', )
    seeds = ('node1.seednodes.xyz', 'node2.seednodes.xyz',
             'node3.seednodes.xyz', 'node4.seednodes.xyz',)
    port = 13373


class EliteTestNet(Elite):
    """
    Class with all the necessary 1337 testing network information based on
    https://github.com/xenonflux/1337/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-elite'
    seeds = ()
    port = 26714
