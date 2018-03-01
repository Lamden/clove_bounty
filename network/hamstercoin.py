from clove.network.bitcoin import Bitcoin


class HamsterCoin(Bitcoin):
    """
    Class with all the necessary HamsterCoin network information based on
    https://github.com/Hamstercoindev/hamstercoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'hamstercoin'
    symbols = ('HAMS', )
    seeds = ("31.131.23.80",
             "31.131.23.80")
    port = 35895
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 42,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 170
    }


class HamsterCoinTestNet(HamsterCoin):
    """
    Class with all the necessary HamsterCoin testing network information based on
    https://github.com/Hamstercoindev/hamstercoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-hamstercoin'
    seeds = ("31.131.23.80",
             "31.131.23.80")
    port = 135895
