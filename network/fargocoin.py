from clove.network.bitcoin import Bitcoin


class Fargocoin(Bitcoin):
    """
    Class with all the necessary Fargocoin (FRGC) network information based on
    https://github.com/fargocoin/fargocoind/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'fargocoin'
    symbols = ('FRGC', )
    seeds = ('138.201.174.79', 'n1.fargochain.org', 'n2.fargochain.org', 'n3.fargochain.org',
             'n4.fargochain.org', 'n5.fargochain.org')
    port = 14451
    message_start = b'\xf9\xbe\xb4\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 35,
        'SECRET_KEY': 128
    }


class FargocoinTestNet(Fargocoin):
    """
    Class with all the necessary Fargocoin (FRGC) testing network information based on
    https://github.com/fargocoin/fargocoind/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-fargocoin'
    seeds = ('138.201.174.79', 'n1.fargochain.org', 'n2.fargochain.org', 'n3.fargochain.org',
             'n4.fargochain.org', 'n5.fargochain.org')
    port = 15451
    message_start = b'\x0b\x11\x09\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 35,
        'SECRET_KEY': 239
    }
