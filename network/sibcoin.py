
from clove.network.bitcoin import Bitcoin


class SibCoin(Bitcoin):
    """
    Class with all the necessary SIB network information based on
    http://www.github.com/ivansib/sibcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'coin'
    symbols = ('SIB', )
    seeds = ('dnsseed.sibcoin.net', 'dnsseed.chervonec.info',
             'dnsseed1.darknode.ru', 'dnsseed2.darknode.ru', 'dnsseed3.darknode.ru')
    port = 1945
    message_start = b'\xbf\x0c\x6b\xbd'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 40,
        'SECRET_KEY': 128
    }


class SibCoinTestNet(SibCoin):
    """
    Class with all the necessary SIB testing network information based on
    http://www.github.com/ivansib/sibcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-coin'
    seeds = ('testnet-seed.dashdot.io', 'test.dnsseed.masternode.io')
    port = 11945
    message_start = b'\xce\xe2\xca\xff'
    base58_prefixes = {
        'PUBKEY_ADDR': 125,
        'SCRIPT_ADDR': 100,
        'SECRET_KEY': 239
    }
