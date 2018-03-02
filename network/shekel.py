from clove.network.bitcoin import Bitcoin


class Shekel(Bitcoin):
    """
    Class with all the necessary Shekel (JEW) network information based on
    https://github.com/shekeltechnologies/JewNew/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'shekel'
    symbols = ('JEW', )
    seeds = ('nodes.shekel.pw', 'shekel.nodes.gyservers.com')
    port = 5500
    message_start = b'\x63\x43\x49\x56'
    base58_prefixes = {
        'PUBKEY_ADDR': 43,
        'SCRIPT_ADDR': 13,
        'SECRET_KEY': 212
    }


class ShekelTestNet(Shekel):
    """
    Class with all the necessary Shekel (JEW) testing network information based on
    https://github.com/shekeltechnologies/JewNew/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-shekel'
    seeds = ()
    nodes = ('207.148.0.129', '45.77.239.30', '45.76.226.204', )
    port = 51434
    message_start = b'\x43\x76\x65\xba'
    base58_prefixes = {
        'PUBKEY_ADDR': 139,
        'SCRIPT_ADDR': 19,
        'SECRET_KEY': 239
    }
