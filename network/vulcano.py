
from clove.network.bitcoin import Bitcoin


class Vulcano(Bitcoin):
    """
    Class with all the necessary VULC network information based on
    https://github.com/vulcanodev/vulcano/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'vulcano'
    symbols = ('VULC', )
    nodes = ('198.136.28.100', )
    port = 21041
    message_start = b'\xe5\x77\x77\x46'
    base58_prefixes = {
        'PUBKEY_ADDR': 70,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 198
    }


class VulcanoTestNet(Vulcano):
    """
    Class with all the necessary VULC testing network information based on
    https://github.com/vulcanodev/vulcano/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-vulcano'
    seeds = ()
    port = 31041
    message_start = b'\x82\x54\x78\x25'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
