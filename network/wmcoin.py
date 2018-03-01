from clove.network.bitcoin import Bitcoin


class Wmcoin(Bitcoin):
    """
    Class with all the necessary WMC network information based on
    https://github.com/wemcoin/wmcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'wmcoin'
    symbols = ('WMC', )
    nodes = ('120.27.114.125', )
    port = 32866
    message_start = b'\xce\xfb\xfa\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 135,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 263
    }


class WmcoinTestNet(Wmcoin):
    """
    Class with all the necessary WMC testing network information based on
    https://github.com/wemcoin/wmcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-wmcoin'
    seeds = ()
    port = 30801
    message_start = b'\xcd\xf1\xc0\xef'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
