from clove.network.bitcoin import Bitcoin


class Spec(Bitcoin):
    """
    Class with all the necessary  SPEC (SPEC) network information based on
    https://github.com/SpecDevelopment/spec-wallet/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'spec'
    symbols = ('SPEC', )
    seeds = ('node.speccoin.com', 'node2.speccoin.com')
    port = 4319
    message_start = b'\xc3\xd2\xd1\xbd'
    base58_prefixes = {
        'PUBKEY_ADDR': 10,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 138
    }


class SpecTestNet(Spec):
    """
    Class with all the necessary  SPEC (SPEC) network information based on
    https://github.com/SpecDevelopment/spec-wallet/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-spec'
    symbols = ('SPEC', )
    seeds = ()
    port = 14319
