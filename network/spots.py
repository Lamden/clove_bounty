from clove.network.bitcoin import Bitcoin


class Spots(Bitcoin):
    """
    Class with all the necessary Spots network information based on
    https://github.com/thespt/spots2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'spots'
    symbols = ('SPT', )
    seeds = ("spots.dnsseed.crypto2.net")
    port = 4588


class SpotsTestNet(Spots):
    """
    Class with all the necessary Spots testing network information based on
    https://github.com/thespt/spots2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-spots'
    seeds = ("dstest.theSPT.com")
    port = 15588
