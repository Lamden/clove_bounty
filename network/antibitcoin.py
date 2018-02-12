
from clove.network.bitcoin import Bitcoin


class AntiBitcoin(Bitcoin):
    """
    Class with all the necessary ANTI network information based on
    https://github.com/antibitcoin/antibitcoin-source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'antibitcoin'
    symbols = ('ANTI', )
    seeds = ('24.37.4188.213.171.167', '108.61.165.75')
    port = 11650


class AntiBitcoinTestNet(AntiBitcoin):
    """
    Class with all the necessary ANTI testing network information based on
    https://github.com/antibitcoin/antibitcoin-source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-antibitcoin'
    seeds = ()
    port = 21650