from clove.network.bitcoin import Bitcoin


class Navcoin(Bitcoin):
    """
    Class with all the necessary NAV Coin (NAV) network information based on
    https://github.com/NAVCoin/navcoin-core/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'navcoin'
    symbols = ('NAV', )
    nodes = ('95.183.51.56', '95.183.52.55', '95.183.52.28',
             '95.183.52.29', '95.183.53.184')
    port = 44440
    message_start = b'\x80\x50\x34\x20'
    base58_prefixes = {
        'PUBKEY_ADDR': 53,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 150
    }


class NavcoinTestNet(Navcoin):
    """
    Class with all the necessary  NAV Coin (NAV) testing network information based on
    https://github.com/NAVCoin/navcoin-core/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-navcoin'
    seeds = ()
    port = 15556
    message_start = b'\x3f\xa2\x52\x20'
    base58_prefixes = {
        'PUBKEY_ADDR': 54,
        'SCRIPT_ADDR': 86,
        'SECRET_KEY': 52
    }
