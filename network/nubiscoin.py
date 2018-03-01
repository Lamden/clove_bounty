from clove.network.bitcoin import Bitcoin


class NubisCoin(Bitcoin):
    """
    Class with all the necessary NubisCoin network information based on
    https://github.com/nubiscoin/codebase/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'nubiscoin'
    symbols = ('NUBIS', )
    seeds = ("seeder1.nubiscoin.xyz",
             "seeder2.nubiscoin.xyz")
    port = 9912
    message_start = b'\xb6\xc1\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 53,
        'SCRIPT_ADDR': 41,
        'SECRET_KEY': 181
    }
