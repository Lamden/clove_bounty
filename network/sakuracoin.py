from clove.network.bitcoin import Bitcoin


class Sakuracoin(Bitcoin):
    """
    Class with all the necessary Sakuracoin network information based on
    https://github.com/sakuracoin-project/sakuracoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'sakuracoin'
    symbols = ('SKR', )
    seeds = ("skrseed.sighash.info")
    port = 9301
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 178
    }


class SakuracoinTestNet(Sakuracoin):
    """
    Class with all the necessary Sakuracoin testing network information based on
    https://github.com/sakuracoin-project/sakuracoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-sakuracoin'
    seeds = ("skrseed.sighash.info")
    port = 19301
    message_start = b'\xfc\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
