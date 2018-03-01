
from clove.network.bitcoin import Bitcoin


class TajCoin(Bitcoin):
    """
    Class with all the necessary TAJ network information based on
    http://www.github.com/Taj-Coin/tajcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'tajcoin'
    symbols = ('TAJ', )
    seeds = (
        'node1.tajcoin.tech', 'node2.tajcoin.tech', 'node3.tajcoin.tech', 'node4.tajcoin.tech',
        'node5.tajcoin.tech', 'node6.tajcoin.tech', 'node7.tajcoin.tech', 'node8.tajcoin.tech',
        'node9.tajcoin.tech'
    )
    port = 10712
    message_start = b'\x7d\x4f\x8b\x4d'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 111
    }


class TajCoinTestNet(TajCoin):
    """
    Class with all the necessary TAJ testing network information based on
    http://www.github.com/Taj-Coin/tajcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-tajcoin'
    seeds = ('test1.tajcoin.tech', )
    port = 71210
    message_start = b'\x42\x6f\xe8\x13'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
