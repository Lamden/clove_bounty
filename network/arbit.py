
from clove.network.bitcoin import Bitcoin


class Arbit(Bitcoin):
    """
    Class with all the necessary ARB network information based on
    https://github.com/arbitcoin/arbit/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'arbit'
    symbols = ('ARB', )
    seeds = ('162.243.203.211', '178.62.56.172')
    port = 31930


class ArbitTestNet(Arbit):
    """
    Class with all the necessary ARB testing network information based on
    https://github.com/arbitcoin/arbit/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-arbit'
    seeds = ()
    port = 31914