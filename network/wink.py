
from clove.network.bitcoin import Bitcoin


class Wink(Bitcoin):
    """
    Class with all the necessary WINK network information based on
    https://github.com/winkchain/wink/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'wink'
    symbols = ('WINK', )
    seeds = ('52.42.186.46')
    port = 37748


class WinkTestNet(Wink):
    """
    Class with all the necessary WINK testing network information based on
    https://github.com/winkchain/wink/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-wink'
    seeds = ()
    port = 37747