
from clove.network.bitcoin import Bitcoin


class ParallelCoin(Bitcoin):
    """
    Class with all the necessary DUO network information based on
    http://www.github.com/marcetin/parallelcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'parallelcoin'
    symbols = ('DUO', )
    seeds = ('seed1.parallelcoin.info', 'seed3.parallelcoin.info',
             'seed2.parallelcoin.info', 'seed4.parallelcoin.info', 'seed5.parallelcoin.info')
    port = 11047
    message_start = b'\xcd\x08\xac\xff'
    base58_prefixes = {
        'PUBKEY_ADDR': 83,
        'SCRIPT_ADDR': 9,
        'SECRET_KEY': 178
    }


class ParallelCoinTestNet(ParallelCoin):
    """
    Class with all the necessary DUO testing network information based on
    http://www.github.com/marcetin/parallelcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-parallelcoin'
    seeds = ('seed2.parallelcoin.info', )
    port = 21047
    message_start = b'\x08\xb2\x99\x88'
    base58_prefixes = {
        'PUBKEY_ADDR': 18,
        'SCRIPT_ADDR': 188,
        'SECRET_KEY': 239
    }
