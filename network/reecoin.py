
from clove.network.bitcoin import Bitcoin


class ReeCoin(Bitcoin):
    """
    Class with all the necessary REE network information based on
    http://www.github.com/Reecoin/Reecoin-Project/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'reecoin'
    symbols = ('REE', )
    nodes = ('192.155.106.33',)
    port = 11300
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 60,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 188
    }


class ReeCoinTestNet(ReeCoin):
    """
    Class with all the necessary REE testing network information based on
    http://www.github.com/Reecoin/Reecoin-Project/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-reecoin'
    nodes = (
        '192.155.106.33', '128.199.88.179', '159.203.77.13', '104.236.121.178', '104.236.230.197', '128.199.158.192',
        '198.199.74.132', '139.59.166.190', '188.166.225.92', '188.166.225.92', '46.101.202.84', '139.59.166.190',
        '159.203.9.117', '192.155.106.33'
    )
    port = 12385
