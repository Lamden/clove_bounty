from clove.network.bitcoin import Bitcoin


class Dream8Coin(Bitcoin):
    """
    Class with all the necessary Dream8Coin network information based on
    https://github.com/dream8coin/dreamcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'dream8coin'
    symbols = ('DMD', )
    seeds = ("seed.ssaomi.com",
             "seed2.ssaomi.com")
    port = 7774
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 176
    }


class Dream8CoinTestNet(Dream8Coin):
    """
    Class with all the necessary Dream8Coin testing network information based on
    https://github.com/dream8coin/dreamcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-diamond'
    seeds = ("tseed.ssaomi.com")
    port = 17774
