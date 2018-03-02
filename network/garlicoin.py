from clove.network.bitcoin import Bitcoin


class Garlicoin(Bitcoin):
    """
    Class with all the necessary Garlicoin (GRLC) network information based on
    https://github.com/GarlicoinOrg/Garlicoin/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'garlicoin'
    symbols = ('GRLC', )
    seeds = ('dnsseed.brennanmcdonald.io', 'dnsseed.rshaw.space', )
    port = 42069
    message_start = b'\xd2\xc6\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 176
    }


class GarlicoinTestNet(Garlicoin):
    """
    Class with all the necessary Garlicoin (GRLC) testing network information based on
    https://github.com/GarlicoinOrg/Garlicoin/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-garlicoin'
    seeds = ('dnsseed-testnet.brennanmcdonald.io',
             'dnsseed-testnet.rshaw.space')
    port = 42075
    message_start = b'\xfd\xd2\xc8\xf2'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
