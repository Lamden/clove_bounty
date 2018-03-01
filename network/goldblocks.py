
from clove.network.bitcoin import Bitcoin


class GoldBlocks(Bitcoin):
    """
    Class with all the necessary GB network information based on
    http://www.github.com/goldblockscoin/goldblocks/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'goldblocks'
    symbols = ('GB', )
    seeds = ('149.56.154.75', '85.25.198.134',
             '198.54.123.200', '185.69.55.38')
    port = 27920
    message_start = b'\x60\xb6\xcd\xf4'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 155
    }


class GoldBlocksTestNet(GoldBlocks):
    """
    Class with all the necessary GB testing network information based on
    http://www.github.com/goldblockscoin/goldblocks/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-goldblocks'
    seeds = ('94.176.238.60', '185.5.53.201', 'node1.goldblocks.eu', 'node2.goldblocks.eu', 'node3.goldblocks.eu',
             'node4.goldblocks.eu', 'node5.goldblocks.eu', 'node6.goldblocks.eu', 'node7.goldblocks.eu')
    port = 27921
    message_start = b'\xd0\xac\x34\x12'
    base58_prefixes = {
        'PUBKEY_ADDR': 97,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
