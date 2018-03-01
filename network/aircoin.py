from clove.network.bitcoin import Bitcoin


class AIRcoin(Bitcoin):
    """
    Class with all the necessary AIRcoin network information based on
    https://github.com/TeamAIRcoin/AIRcoin/blob/master/src/net.cpp#L17
    (date of access: 02/13/2018)
    """
    name = 'aircoin'
    symbols = ('AIR', )
    seeds = ("dnsseed.aircointools.org",
             "aircointools.com",
             "dnsseed.ltc.xurious.com",
             "dnsseed.koin-project.com",
             "dnsseed.weminemnc.com")
    port = 1631
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 151
    }


class AIRcoinTestNet(AIRcoin):
    """
    Class with all the necessary AIRcoin testing network information based on
    https://github.com/TeamAIRcoin/AIRcoin/blob/master/src/net.cpp#L17
    (date of access: 02/13/2018)
    """
    name = 'test-aircoin'
    seeds = ("testnet-seed.AIRcointools.com",
             "testnet-seed.weminemnc.com")
    port = 1632
    message_start = b'\xfc\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
