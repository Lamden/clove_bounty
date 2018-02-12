
from clove.network.bitcoin import Bitcoin


class Kurrent(Bitcoin):
    """
    Class with all the necessary KURT network information based on
    http://www.github.com/kurrentproject/Kurrent/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'kurrent'
    symbols = ('KURT', )
    seeds = ('212.24.107.99',)
    port = 18080


class KurrentTestNet(Kurrent):
    """
    Class with all the necessary KURT testing network information based on
    http://www.github.com/kurrentproject/Kurrent/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-kurrent'
    seeds = ()
    port = 28080
