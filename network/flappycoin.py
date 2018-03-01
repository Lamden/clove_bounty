from clove.network.bitcoin import Bitcoin


class Flappycoin(Bitcoin):
    """
    Class with all the necessary Flappycoin (FLAP) network information based on
    https://github.com/flappycoin-project/flappycoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'flappycoin'
    symbols = ('FLAP', )
    seeds = ('seed.terracoin.io', 'dnsseed.flap.so')
    port = 11556
    message_start = b'\xc1\xc1\xc1\xc1'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 163
    }


class FlappycoinTestNet(Flappycoin):
    """
    Class with all the necessary Flappycoin (FLAP) testing network information based on
    https://github.com/flappycoin-project/flappycoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-flappycoin'
    seeds = ('dnsseed.flap.so', )
    port = 33556
    message_start = b'\xfc\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
