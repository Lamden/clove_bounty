
from clove.network.bitcoin import Bitcoin


class Bitcore(Bitcoin):
    """
    Class with all the necessary BTX network information based on
    http://www.github.com/LIMXTEC/BitCore/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'bitcore'
    symbols = ('BTX', )
    seeds = ('188.68.52.172', '37.120.186.85', '37.120.190.76')
    port = 8555


class BitcoreTestNet(Bitcore):
    """
    Class with all the necessary BTX testing network information based on
    http://www.github.com/LIMXTEC/BitCore/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-bitcore'
    seeds = ('188.68.52.172', '37.120.186.85', '37.120.190.76', 'dnsseed1.bitcore.org', 'dnsseed2.bitcore.org')
    port = 18333
