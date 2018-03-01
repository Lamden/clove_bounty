from clove.network.bitcoin import Bitcoin


class KekCoin(Bitcoin):
    """
    Class with all the necessary KekCoin network information based on
    https://github.com/Kekcoin-Core/kekcoin-segwit/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'kekcoin'
    symbols = ('KEK', )
    seeds = ("107.191.48.186",
             "209.250.246.178",
             "209.250.246.85")
    port = 13337
    message_start = b'\x11\x22\x33\x44'
    base58_prefixes = {
        'PUBKEY_ADDR': 45,
        'SCRIPT_ADDR': 88,
        'SECRET_KEY': 133
    }


class KekCoinTestNet(KekCoin):
    """
    Class with all the necessary KekCoin testing network information based on
    https://github.com/Kekcoin-Core/kekcoin-segwit/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-kekcoin'
    seeds = ("209.250.246.85")
    port = 13777
    message_start = b'\x55\x66\x77\x88'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
