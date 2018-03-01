from clove.network.bitcoin import Bitcoin


class IrishCoin(Bitcoin):
    """
    Class with all the necessary IrishCoin network information based on
    https://github.com/irishcoinproject/irishcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'irishcoin'
    symbols = ('IRL', )
    seeds = ('node.irishcoin.org', 'dns.irishcoin.org', )
    port = 12375
    message_start = b'\xf7\xc1\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 161
    }


class IrishCoinTestNet(IrishCoin):
    """
    Class with all the necessary IrishCoin testing network information based on
    https://github.com/irishcoinproject/irishcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-irishcoin'
    seeds = ('testnode.irishcoin.org', 'testdns.irishcoin.org', )
    port = 11375
    message_start = b'\xfc\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
