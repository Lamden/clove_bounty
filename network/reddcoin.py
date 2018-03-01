
from clove.network.bitcoin import Bitcoin


class ReddCoin(Bitcoin):
    """
    Class with all the necessary RDD network information based on
    http://www.github.com/reddcoin-project/reddcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'reddcoin'
    symbols = ('RDD', )
    seeds = ('seed.reddcoin.com', 'dnsseed01.redd.ink',
             'dnsseed02.redd.ink', 'dnsseed03.redd.ink')
    port = 45444
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 61,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 189
    }


class ReddCoinTestNet(ReddCoin):
    """
    Class with all the necessary RDD testing network information based on
    http://www.github.com/reddcoin-project/reddcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-reddcoin'
    seeds = ('testnet-seed.reddcoin.com', 'testnet-dnsseed.redd.ink')
    port = 55444
    message_start = b'\xfe\xc3\xb9\xde'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
