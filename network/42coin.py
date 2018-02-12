
from clove.network.bitcoin import Bitcoin


class Coin42(Bitcoin):
    """
    Class with all the necessary 42 network information based on
    https://github.com/42-coin/42/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = '42-coin'
    symbols = ('42', )
    seeds = ()
    port = 4242


class Coin42TestNet(Coin42):
    """
    Class with all the necessary 42 testing network information based on
    https://github.com/42-coin/42/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-42-coin'
    seeds = ()
    port = 42420