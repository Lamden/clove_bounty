from clove.network.bitcoin import Bitcoin


class Nexus(Bitcoin):
    """
    Class with all the necessary Nexus NXS network information based on
    https://github.com/Nexusoft/Nexus/blob/master/src/net/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'nexus'
    symbols = ('NXS', )
    seeds = ('204.27.62.234')
    port = 9323
    message_start = b'\xe9\x59\x0d\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 42,
        'SCRIPT_ADDR': 104,
        'SECRET_KEY': 170
    }


class NexusTestNet(Nexus):
    """
    Class with all the necessary Nexus NXS testing network information based on
    https://github.com/Nexusoft/Nexus/blob/master/src/net/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-nexus'
    seeds = ()
    port = 8313
    message_start = b'\x05\x0d\x59\xe9'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
