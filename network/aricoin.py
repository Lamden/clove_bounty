
from clove.network.bitcoin import Bitcoin


class Aricoin(Bitcoin):
    """
    Class with all the necessary ARI network information based on
    http://www.github.com/aricoin/aricoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'aricoin'
    symbols = ('ARI', )
    seeds = ('seed.aricoin.com',)
    port = 16567
    message_start = b'\xc2\xdb\xf1\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 11,
        'SCRIPT_ADDR': 22,
        'SECRET_KEY': 158
    }


class AricoinTestNet(Aricoin):
    """
    Class with all the necessary ARI testing network information based on
    http://www.github.com/aricoin/aricoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-aricoin'
    seeds = ('seed.mophides.com', 'seed.dglibrary.org', 'seed.arichain.info',
             'testari-seed.lionservers.de', 'testari-seed-static.lionservers.de')
    port = 26567
    message_start = b'\xc2\xdb\xf1\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 11,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 241
    }
