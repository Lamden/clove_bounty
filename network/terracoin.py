from clove.network.bitcoin import Bitcoin


class Terracoin(Bitcoin):
    """
    Class with all the necessary Terracoin (TRC) network information based on
    https://github.com/terracoin/terracoin/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'terracoin'
    symbols = ('TRC', )
    seeds = ('seed.terracoin.io', 'dnsseed.southofheaven.ca', )
    port = 13333
    message_start = b'\x42\xba\xbe\x56'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


class TerracoinTestNet(Terracoin):
    """
    Class with all the necessary Terracoin (TRC) testing network information based on
    https://github.com/terracoin/terracoin/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-terracoin'
    seeds = ('testnetseed.terracoin.io', )
    port = 18321
    message_start = b'\x0b\x11\x09\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
