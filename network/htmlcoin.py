from clove.network.bitcoin import Bitcoin


class HTMLCOIN(Bitcoin):
    """
    Class with all the necessary HTMLCOIN network information based on
    https://github.com/HTMLCOIN/HTMLCOIN/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'htmlcoin'
    symbols = ('HTML', )
    seeds = ("seed1.htmlcoin.com",
             "seed2.htmlcoin.com",
             "seed3.htmlcoin.com",
             "seed4.htmlcoin.com")
    port = 4888
    message_start = b'\x1f\x2e\x3d\x4c'
    base58_prefixes = {
        'PUBKEY_ADDR': 41,
        'SCRIPT_ADDR': 100,
        'SECRET_KEY': 169
    }


class HTMLCOINTestNet(HTMLCOIN):
    """
    Class with all the necessary HTMLCOIN testing network information based on
    https://github.com/HTMLCOIN/HTMLCOIN/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-htmlcoin'
    seeds = ("testnet-seed1.htmlcoin.com", "testnet-seed2.htmlcoin.com", )
    port = 14888
    message_start = b'\x2f\x3e\x4d\x5c'
    base58_prefixes = {
        'PUBKEY_ADDR': 100,
        'SCRIPT_ADDR': 110,
        'SECRET_KEY': 228
    }
