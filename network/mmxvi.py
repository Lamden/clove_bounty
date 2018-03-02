
from clove.network.bitcoin import Bitcoin


class MMXVI(Bitcoin):
    """
    Class with all the necessary MMXVI network information based on
    http://www.github.com/coin2016/MMXVI/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'mmxvi'
    symbols = ('MMXVI', )
    nodes = ('5.196.67.100', )
    port = 6503
    message_start = b'\xc3\xff\xd2\xb4'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 178
    }


class MMXVITestNet(MMXVI):
    """
    Class with all the necessary MMXVI testing network information based on
    http://www.github.com/coin2016/MMXVI/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-mmxvi'
    seeds = ('dnsseed.MMXVI.org', )
    port = 16503
    message_start = b'\xa1\xbb\xd1\xf8'
    base58_prefixes = {
        'PUBKEY_ADDR': 112,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 240
    }
