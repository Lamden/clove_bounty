
from clove.network.bitcoin import Bitcoin


class Animecoin(Bitcoin):
    """
    Class with all the necessary ANI network information based on
    http://www.github.com/testzcrypto/Animecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'animecoin'
    symbols = ('ANI', )
    nodes = (
        '96.43.130.251', '91.121.8.23', '62.210.151.205', '222.78.67.174', '5.9.158.79', '186.237.174.48',
        '82.117.232.30', '151.236.22.84', '158.255.208.40', '151.236.15.106', '91.121.8.23', '213.183.56.176',
        '151.236.13.37', '115.29.49.156'
    )
    port = 1212


class AnimecoinTestNet(Animecoin):
    """
    Class with all the necessary ANI testing network information based on
    http://www.github.com/testzcrypto/Animecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-animecoin'
    seeds = ()
    port = 2424
