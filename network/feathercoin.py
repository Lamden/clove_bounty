from clove.network.bitcoin import Bitcoin


class Feathercoin(Bitcoin):
    """
    Class with all the necessary Feathercoin network information based on
    https://github.com/FeatherCoin/Feathercoin/blob/master-0.13/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'feathercoin'
    symbols = ('FTC', )
    seeds = ("dnsseed.feathercoin.com",
             "explorer2.feathercoin.com",
             "dnsseed.alltheco.in",
             "block.ftc-c.com",
             "dnsseed-static.feathercoin.ch")
    port = 9336
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 14,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 142
    }


class FeathercoinTestNet(Feathercoin):
    """
    Class with all the necessary Feathercoin testing network information based on
    https://github.com/FeatherCoin/Feathercoin/blob/master-0.13/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-feathercoin'
    seeds = ("testnet-explorer2.feathercoin.com",
             "testnet-dnsseed.feathercoin.com")
    port = 19336
    message_start = b'\xda\xaf\xa5\xba'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
