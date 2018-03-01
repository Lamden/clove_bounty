from clove.network.bitcoin import Bitcoin


class Woodcoin(Bitcoin):
    """
    Class with all the necessary Woodcoin (LOG) network information based on
    https://github.com/funkshelper/woodcore/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'woodcoin'
    symbols = ('LOG', )
    seeds = ('dnsseed.woodcoin.org', )
    port = 8338
    message_start = b'\xfc\xd9\xb7\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 73,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 201
    }


class WoodcoinTestNet(Woodcoin):
    """
    Class with all the necessary Woodcoin (LOG) testing network information based on
    https://github.com/funkshelper/woodcore/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-woodcoin'
    seeds = ('dnsseed.woodcointools.com', )
    port = 18338
    message_start = b'\xfc\xd9\xb7\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 135,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 199
    }
