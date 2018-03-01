
from clove.network.bitcoin import Bitcoin


class GeyserCoin(Bitcoin):
    """
    Class with all the necessary GSR network information based on
    http://www.github.com/geysercoin/geysercoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'geysercoin'
    symbols = ('GSR', )
    seeds = ('nodea.geysercoin.com',
             'nodeb.geysercoin.com', 'nodec.geysercoin.com')
    port = 10556
    message_start = b'\x60\x34\x12\x08'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 63,
        'SECRET_KEY': 171
    }


class GeyserCoinTestNet(GeyserCoin):
    """
    Class with all the necessary GSR testing network information based on
    http://www.github.com/geysercoin/geysercoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-geysercoin'
    seeds = ()
    port = 20556
    message_start = b'\xad\xf4\xd0\xac'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
