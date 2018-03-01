from clove.network.bitcoin import Bitcoin


class Mincoin(Bitcoin):
    """
    Class with all the necessary Mincoin network information based on
    https://github.com/mincoin/mincoin/blob/0.8/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'mincoin'
    symbols = ('MNC', )
    seeds = ("seed.mincointools.com",
             "seed.mincoinpool.org")
    port = 9334
    message_start = b'\x63\x42\x21\x2c'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 178
    }


class MincoinTestNet(Mincoin):
    """
    Class with all the necessary Mincoin testing network information based on
    https://github.com/mincoin/mincoin/blob/0.8/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-mincoin'
    seeds = ("testnet-seed.mincointools.com",
             "testnet-seed.mincoinpool.org")
    port = 19334
    message_start = b'\x63\xf2\xc0\x2c'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
