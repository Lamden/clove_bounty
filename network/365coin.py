from clove.network.bitcoin import Bitcoin


class Three65Coin(Bitcoin):
    """
    Class with all the necessary  365Coin (365) network information based on
    https://github.com/365coindev/365/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = '365coin'
    symbols = ('365', )
    seeds = ('198.199.90.93')
    port = 15663
    message_start = b'\xb7\xf5\xe4\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 13,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 141
    }


class Three65CoinTestNet(Three65Coin):
    """
    Class with all the necessary  365Coin (365) network information based on
    https://github.com/365coindev/365/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-365coin'
    symbols = ('365', )
    seeds = ()
    port = 17778
