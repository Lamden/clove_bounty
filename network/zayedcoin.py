
from clove.network.bitcoin import Bitcoin


class Zayedcoin(Bitcoin):
    """
    Class with all the necessary ZYD network information based on
    http://www.github.com/ZayedCoin/Zayedcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'zayedcoin'
    symbols = ('ZYD', )
    seeds = ('node.zayedcoin.net', 'node1.zayedcoin.net',
             'node2.zayedcoin.net', 'node3.zayedcoin.net', 'node4.zayedcoin.net')
    port = 8371
    message_start = b'\xd0\xce\xcf\x9c'
    base58_prefixes = {
        'PUBKEY_ADDR': 81,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 209
    }
