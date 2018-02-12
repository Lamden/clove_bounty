
from clove.network.bitcoin import Bitcoin


class Warp(Bitcoin):
    """
    Class with all the necessary WARP network information based on
    https://github.com/shapetwist/warp/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'warp'
    symbols = ('WARP', )
    seeds = ('84.200.4.70')
    port = 31312


class WarpTestNet(Warp):
    """
    Class with all the necessary WARP testing network information based on
    https://github.com/shapetwist/warp/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-warp'
    seeds = ()
    port = 31313