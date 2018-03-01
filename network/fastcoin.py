
from clove.network.bitcoin import Bitcoin


class Fastcoin(Bitcoin):
    """
    Class with all the necessary FST network information based on
    http://www.github.com/fastcoinproject/fastcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'fastcoin'
    symbols = ('FST', )
    seeds = ('s1.fastcoin.ws', 'u2.fastcoin.ws', 'a1.fastcoin.ws')
    port = 9526
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 96,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 224
    }


class FastcoinTestNet(Fastcoin):
    """
    Class with all the necessary FST testing network information based on
    http://www.github.com/fastcoinproject/fastcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-fastcoin'
    seeds = ('dnsseed.fastcoinpool.org', 'dnsseed.weminemnc.combase58Prefixes[PUBKEY_ADDRESS]=list_of96',
             'testnet-seed.fastcointools.com', 'testnet-seed.ltc.xurious.com', 'dnsseed.wemine-testnet.com')
    port = 19526
    message_start = b'\xfc\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
