
from clove.network.bitcoin import Bitcoin


class CthulhuOfferings(Bitcoin):
    """
    Class with all the necessary OFF network information based on
    http://www.github.com/thegreatoldone/offerings/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'cthulhuofferings'
    symbols = ('OFF', )
    seeds = ('144.76.91.109',)
    port = 20000


class CthulhuOfferingsTestNet(CthulhuOfferings):
    """
    Class with all the necessary OFF testing network information based on
    http://www.github.com/thegreatoldone/offerings/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-cthulhuofferings'
    seeds = ('',)
    port = 21973
