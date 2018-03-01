from clove.network.bitcoin import Bitcoin


class ION(Bitcoin):
    """
    Class with all the necessary ION (ION) network information based on
    https://github.com/ionomy/ion/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'ion'
    symbols = ('ION', )
    seeds = ('main.seeder.baseserv.com', 'main.seeder.uksafedns.net')
    port = 12700
    message_start = b'\xc4\xe1\xd8\xec'
    base58_prefixes = {
        'PUBKEY_ADDR': 103,
        'SCRIPT_ADDR': 88,
        'SECRET_KEY': 153
    }


class IONTestNet(ION):
    """
    Class with all the necessary ION (ION) testing network information based on
    https://github.com/ionomy/ion/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-ion'
    seeds = ('testnet.seeder.baseserv.com', 'testnet.seeder.uksafedns.net')
    port = 27170
    message_start = b'\xdb\x86\xfc\x69'
    base58_prefixes = {
        'PUBKEY_ADDR': 97,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
