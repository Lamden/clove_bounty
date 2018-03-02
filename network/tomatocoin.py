from clove.network.bitcoin import Bitcoin


class Tomatocoin(Bitcoin):
    """
    Class with all the necessary Tomatocoin network information based on
    https://github.com/Tomatocoin/tomatocoin-master/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'tomatocoin'
    symbols = ('TMT', )
    nodes = ("23.23.186.131", )
    port = 9888
    message_start = b'\xbf\x0c\x6b\xbd'
    base58_prefixes = {
        'PUBKEY_ADDR': 66,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 194
    }


class TomatocoinTestNet(Tomatocoin):
    """
    Class with all the necessary Tomatocoin testing network information based on
    https://github.com/Tomatocoin/tomatocoin-master/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'test-tomatocoin'
    nodes = ("23.23.186.131", )
    port = 19888
    message_start = b'\xce\xe2\xca\xff'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
