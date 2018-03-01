from clove.network.bitcoin import Bitcoin


class DuckDuckCoin(Bitcoin):
    """
    Class with all the necessary DuckDuckCoin network information based on
    https://github.com/duckduckcoin/duckduckcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'duckduckcoin'
    symbols = ('DUCK', )
    seeds = ("node1.duckduckcoin.com")
    port = 17771
    message_start = b'\x6c\x2d\x24\x24'
    base58_prefixes = {
        'PUBKEY_ADDR': 90,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 218
    }


class DuckDuckCoinTestNet(DuckDuckCoin):
    """
    Class with all the necessary DuckDuckCoin testing network information based on
    https://github.com/duckduckcoin/duckduckcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-duckduckcoin'
    seeds = ("testnode1.duckduckcoin.com")
    port = 51474
