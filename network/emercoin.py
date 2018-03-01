from clove.network.bitcoin import Bitcoin


class Emercoin(Bitcoin):
    """
    Class with all the necessary Emercoin EMC network information based on
    https://github.com/emercoin/emercoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'emercoin'
    symbols = ('EMC', )
    seeds = ('seed.emercoin.com', 'seed.emercoin.net',
             'seed.emergate.net', 'seed.emc')
    port = 6661
    message_start = b'\xe6\xe8\xe9\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 92,
        'SECRET_KEY': 128
    }


class EmercoinTestNet(Emercoin):
    """
    Class with all the necessary Emercoin EMC testing network information based on
    https://github.com/emercoin/emercoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-emercoin'
    seeds = ('tnseed.emercoin.com')
    port = 6663
    message_start = b'\xcb\xf2\xc0\xef'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
