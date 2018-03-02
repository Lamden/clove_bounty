from clove.network.bitcoin import Bitcoin


class TopazCoin(Bitcoin):
    """
    Class with all the necessary  Topaz Coin (TOPAZ) network information based on
    https://github.com/CryptoCoderz/TOPAZ/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'topazcoin'
    symbols = ('TOPAZ', )
    nodes = ('91.134.120.210', )
    port = 6909
    message_start = b'\xea\x92\x66\xe4'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 97,
        'SECRET_KEY': 42
    }


class TopazCoinTestNet(TopazCoin):
    """
    Class with all the necessary  Topaz Coin (TOPAZ) network information based on
    https://github.com/CryptoCoderz/TOPAZ/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-topazcoin'
    symbols = ('TOPAZ', )
    seeds = ()
    port = 6808
    message_start = b'\x93\xe1\xaa\xb8'
    base58_prefixes = {
        'PUBKEY_ADDR': 66,
        'SCRIPT_ADDR': 41,
        'SECRET_KEY': 33
    }
