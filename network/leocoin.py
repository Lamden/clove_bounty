from clove.network.bitcoin import Bitcoin


class LEOcoin(Bitcoin):
    """
    Class with all the necessary LEO network information based on
    http://www.github.com/Leocoin-project/LEOcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'leocoin'
    symbols = ('LEO', )
    seeds = (
        'dnsseed.leocoin.org', 'leoseed.leocoin.org', 'node1.leocoin.org', 'node2.leocoin.org', 'node3.leocoin.org',
        'node4.leocoin.org', 'node5.leocoin.org', 'node6.leocoin.org', 'node7.leocoin.org', 'node8.leocoin.org',
        'node9.leocoin.org', 'node10.leocoin.org'
    )
    port = 5840
    message_start = b'\x64\x6e\x78\x82'
    base58_prefixes = {
        'PUBKEY_ADDR': 18,
        'SCRIPT_ADDR': 88,
        'SECRET_KEY': 144
    }


class LEOcoinTestNet(LEOcoin):
    """
    Class with all the necessary LEO testing network information based on
    http://www.github.com/Leocoin-project/LEOcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-leocoin'
    seeds = ()
    port = 15840
    message_start = b'\x8c\x96\xa0\xaa'
    base58_prefixes = {
        'PUBKEY_ADDR': 66,
        'SCRIPT_ADDR': 76,
        'SECRET_KEY': 194
    }
