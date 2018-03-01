from clove.network.bitcoin import Bitcoin


class Birds(Bitcoin):
    """
    Class with all the necessary  Birds (BIRDS) network information based on
    https://github.com/Birdsdev/Birds/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'birds'
    symbols = ('BIRDS', )
    seeds = ('104.200.67.124')
    port = 20013
    message_start = b'\x17\xf7\xfe\xdf'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }


class BirdsTestNet(Birds):
    """
    Class with all the necessary  Birds (BIRDS) network information based on
    https://github.com/Birdsdev/Birds/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-birds'
    symbols = ('BIRDS', )
    seeds = ()
    port = 30013
