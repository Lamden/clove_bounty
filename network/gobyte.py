
from clove.network.bitcoin import Bitcoin


class GoByte(Bitcoin):
    """
    Class with all the necessary GBX network information based on
    http://www.github.com/gobytecoin/gobyte/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'gobyte'
    symbols = ('GBX', )
    seeds = ('seed1.gobyte.network', 'seed2.gobyte.network',
             'seed3.gobyte.network', 'seed4.gobyte.network')
    port = 12455


class GoByteTestNet(GoByte):
    """
    Class with all the necessary GBX testing network information based on
    http://www.github.com/gobytecoin/gobyte/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-gobyte'
    seeds = ('testnet-dns.gobyte.network', 'testnet2-dns.gobyte.network')
    port = 13455
