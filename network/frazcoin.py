from clove.network.bitcoin import Bitcoin


class Frazcoin(Bitcoin):
    """
    Class with all the necessary Frazcoin network information based on
    https://github.com/frazcoin/frazCoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'frazcoin'
    symbols = ('FRAZ', )
    seeds = ("frazcoin.eu")
    port = 3991
    message_start = b'\x46\x52\x41\x5A'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 163
    }


class FrazcoinTestNet(Frazcoin):
    """
    Class with all the necessary Frazcoin testing network information based on
    https://github.com/frazcoin/frazCoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-frazcoin'
    seeds = ("frazcoin.eu")
    port = 3981
    message_start = b'\x5A\x41\x52\x46'
    base58_prefixes = {
        'PUBKEY_ADDR': 95,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 223
    }
