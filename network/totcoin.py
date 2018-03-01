from clove.network.bitcoin import Bitcoin


class TotCoin(Bitcoin):
    """
    Class with all the necessary TotCoin network information based on
    https://github.com/totcoindev/totcoin/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'totcoin'
    symbols = ('TOT', )
    seeds = ("78.113.252.129")
    port = 42400
    message_start = b'\xbf\x0c\x6b\xbd'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 16,
        'SECRET_KEY': 204
    }


class TotCoinTestNet(TotCoin):
    """
    Class with all the necessary TotCoin testing network information based on
    https://github.com/totcoindev/totcoin/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-totcoin'
    seeds = ("soscoindev.ddns.net")
    port = 19999
    message_start = b'\xce\xe2\xca\xff'
    base58_prefixes = {
        'PUBKEY_ADDR': 140,
        'SCRIPT_ADDR': 19,
        'SECRET_KEY': 239
    }
