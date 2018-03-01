from clove.network.bitcoin import Bitcoin


class YAYcoin(Bitcoin):
    """
    Class with all the necessary YAYcoin network information based on
    https://github.com/dkwzjw/yaycoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'yaycoin'
    symbols = ('YAY', )
    seeds = ("yaycoin.sun.ddns.vc",
             "yaycoin.luna.ddns.vc")
    port = 7785
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 78,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 206
    }


class YAYcoinTestNet(YAYcoin):
    """
    Class with all the necessary YAYcoin testing network information based on
    https://github.com/dkwzjw/yaycoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-yaycoin'
    seeds = ("yaycoin.sun.ddns.vc",
             "yaycoin.luna.ddns.vc")
    port = 17785
    message_start = b'\xfc\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
