
from clove.network.bitcoin import Bitcoin


class WomenCoin(Bitcoin):
    """
    Class with all the necessary WOMEN network information based on
    https://github.com/womencoin/womencoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'womencoin'
    symbols = ('WOMEN', )
    seeds = ('104.200.67.104')
    port = 19207
    message_start = b'\xf1\x13\x94\xee'
    base58_prefixes = {
        'PUBKEY_ADDR': 73,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 201
    }


class WomenCoinTestNet(WomenCoin):
    """
    Class with all the necessary WOMEN testing network information based on
    https://github.com/womencoin/womencoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-womencoin'
    seeds = ()
    port = 29207
    message_start = b'\x00\x24\x7f\x1e'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
