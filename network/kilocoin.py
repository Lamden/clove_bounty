from clove.network.bitcoin import Bitcoin


class Kilocoin(Bitcoin):
    """
    Class with all the necessary Kilocoin (KLC) network information based on
    https://github.com/kilocoin/kilocoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'kilocoin'
    symbols = ('KLC', )
    seeds = ('dnsseed.kilocoin.com', )
    port = 3112
    message_start = b'\xfc\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 47,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 175
    }


class KilocoinTestNet(Kilocoin):
    """
    Class with all the necessary Kilocoin (KLC) testing network information based on
    https://github.com/kilocoin/kilocoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-kilocoin'
    seeds = ('testnet-seed.kilocoin.com', )
    port = 63112
    message_start = b'\xfd\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
