
from clove.network.bitcoin import Bitcoin


class Vulcano(Bitcoin):
    """
    Class with all the necessary VULC network information based on
    https://github.com/vulcanodev/vulcano/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'vulcano'
    symbols = ('VULC', )
    seeds = ('198.136.28.100')
    port = 21041


class VulcanoTestNet(Vulcano):
    """
    Class with all the necessary VULC testing network information based on
    https://github.com/vulcanodev/vulcano/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-vulcano'
    seeds = ()
    port = 31041