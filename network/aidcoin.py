from clove.network.bitcoin import Bitcoin


class AidCoin(Bitcoin):
    """
    Class with all the necessary AidCoin network information based on
    https://github.com/kreatorpt/aidcoins/blob/master-0.8/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'aidcoin'
    symbols = ('AID', )
    seeds = (
        'dnsseed.aidcoinstools.com',
        'dnsseed.aidcoinspool.org',
        'dnsseed.ltc.xurious.com',
        'dnsseed.koin-project.com',
        'dnsseed.weminemnc.com',
    )
    port = 12223
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 176
    }


class AidCoinTestNet(AidCoin):
    """
    Class with all the necessary AidCoin testing network information based on
    https://github.com/kreatorpt/aidcoins/blob/master-0.8/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'test-aidcoin'
    seeds = (
        'testnet-seed.aidcoinstools.com',
        'testnet-seed.ltc.xurious.com',
        'dnsseed.wemine-testnet.com',
    )
    port = 13330
