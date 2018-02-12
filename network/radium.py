
from clove.network.bitcoin import Bitcoin


class Radium(Bitcoin):
    """
    Class with all the necessary RADS network information based on
    http://www.github.com/RadiumCore/radium-0.11/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'radium'
    symbols = ('RADS', )
    seeds = ('52.23.134.122',)
    port = 27913


class RadiumTestNet(Radium):
    """
    Class with all the necessary RADS testing network information based on
    http://www.github.com/RadiumCore/radium-0.11/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-radium'
    seeds = ('35.153.123.156', '34.207.38.233')
    port = 47963
