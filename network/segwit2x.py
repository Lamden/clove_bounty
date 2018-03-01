from clove.network.bitcoin import Bitcoin


class SegWit2X(Bitcoin):
    """
    Class with all the necessary SegWit2X (B2X) network information based on
    https://github.com/SegwitB2X/bitcoin2x/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'segwit2x'
    symbols = ('B2X', )
    seeds = ('node1.b2x-segwit.io',
             'node2.b2x-segwit.io', 'node3.b2x-segwit.io')
    port = 8333
    message_start = b'\xf4\xb2\xb5\xd8'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


class SegWit2XTestNet(SegWit2X):
    """
    Class with all the necessary SegWit2X (B2X) testing network information based on
    https://github.com/SegwitB2X/bitcoin2x/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-segwit2x'
    seeds = ('node1.b2x-segwit.io',
             'node2.b2x-segwit.io', 'node3.b2x-segwit.io')
    port = 18333
    message_start = b'\xf3\xb1\xb4\xd7'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
