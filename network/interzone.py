from clove.network.bitcoin import Bitcoin


class Interzone(Bitcoin):
    """
    Class with all the necessary Interzone (ITZ) network information based on
    https://github.com/projectinterzone/ITZ/blob/master/src/chainparams.cpp
    (date of access: 02/22/2018)
    """
    name = 'interzone'
    symbols = ('ITZ', )
    seeds = ('seed1.interzone.space',
             'seed2.interzone.space',
             'seed3.interzone.space',
             'seed4.interzone.space',
             'seed5.interzone.space')
    port = 55675
    message_start = b'\x08\x02\x01\x17'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 156
    }


class InterzoneTestNet(Interzone):
    """
    Class with all the necessary Interzone (ITZ) testing network information based on
    https://github.com/projectinterzone/ITZ/blob/master/src/chainparams.cpp
    (date of access: 02/22/2018)
    """
    name = 'test-interzone'
    seeds = ('seed1.interzone.space')
    port = 21817
    message_start = b'\xfb\xc2\x11\x02'
    base58_prefixes = {
        'PUBKEY_ADDR': 102,
        'SCRIPT_ADDR': 44,
        'SECRET_KEY': 216
    }
