from clove.network.bitcoin import Bitcoin


class Syndicate(Bitcoin):
    """
    Class with all the necessary  Syndicate (SYNX) network information based on
    https://github.com/SyndicateLtd/SyndicateQT/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'syndicate'
    symbols = ('SYNX', )
    seeds = ('seed.synx.online')
    port = 9999
    message_start = b'\xd2\x2d\x1c\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }


class SyndicateTestNet(Syndicate):
    """
    Class with all the necessary  Syndicate (SYNX) network information based on
    https://github.com/SyndicateLtd/SyndicateQT/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-syndicate'
    symbols = ('SYNX', )
    seeds = ('')
    port = 27170
    message_start = b'\x2f\xca\x4d\x3e'
    base58_prefixes = {
        'PUBKEY_ADDR': 97,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
