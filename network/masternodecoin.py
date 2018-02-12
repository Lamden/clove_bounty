
from clove.network.bitcoin import Bitcoin


class Masternodecoin(Bitcoin):
    """
    Class with all the necessary MTNC network information based on
    http://www.github.com/masternodecoin/masternodecoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'masternodecoin'
    symbols = ('MTNC', )
    seeds = ('47.52.46.158', '23.247.2.51')
    port = 10086


class MasternodecoinTestNet(Masternodecoin):
    """
    Class with all the necessary MTNC testing network information based on
    http://www.github.com/masternodecoin/masternodecoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-masternodecoin'
    seeds = ()
    port = 11111
