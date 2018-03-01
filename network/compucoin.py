from clove.network.bitcoin import Bitcoin


class CompuCoin(Bitcoin):
    """
    Class with all the necessary CompuCoin network information based on
    https://github.com/compucoin/compucoin/blob/master/src/net.cpp#L12
    (date of access: 02/14/2018)
    """
    name = 'compucoin'
    symbols = ('CPN', )
    seeds = ("209.188.7.177")
    port = 45444
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 156
    }


class CompuCoinTestNet(CompuCoin):
    """
    Class with all the necessary CompuCoin testing network information based on
    https://github.com/compucoin/compucoin/blob/master/src/net.cpp#L12
    (date of access: 02/14/2018)
    """
    name = 'test-compucoin'
    seeds = ("testnet-seed.compucoin.com")
    port = 55444
    message_start = b'\xfc\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
