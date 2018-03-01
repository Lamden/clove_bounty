from clove.network.bitcoin import Bitcoin


class SpreadCoin(Bitcoin):
    """
    Class with all the necessary SpreadCoin network information based on
    https://github.com/spreadcoin/spreadcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'spreadcoin'
    symbols = ('SPR', )
    seeds = ("dnsseed.spreadcoin.net")
    port = 41678
    message_start = b'\x4f\x3c\x5c\xbb'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 191
    }


class SpreadCoinTestNet(SpreadCoin):
    """
    Class with all the necessary SpreadCoin testing network information based on
    https://github.com/spreadcoin/spreadcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-spreadcoin'
    seeds = ("testnet-seed.darkcoin.io", "testnet-seed.darkcoin.qa")
    port = 51678
    message_start = b'\xc2\xe3\xcb\xfa'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
