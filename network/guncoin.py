from clove.network.bitcoin import Bitcoin


class Guncoin(Bitcoin):
    """
    Class with all the necessary Guncoin network information based on
    https://github.com/guncoin/guncoin/blob/master-1.4/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'guncoin'
    symbols = ('GUN', )
    seeds = ("seed.guncoin.info", "seed2.guncoin.info")
    port = 42954
    message_start = b'\xaa\xc3\xc6\xab'
    base58_prefixes = {
        'PUBKEY_ADDR': 39,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 167
    }


class GuncoinTestNet(Guncoin):
    """
    Class with all the necessary Guncoin testing network information based on
    https://github.com/guncoin/guncoin/blob/master-1.4/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-guncoin'
    seeds = ("testnet-seed.guncoin.info", "testnet-seed2.guncoin.info")
    port = 52954
    message_start = b'\xdd\xbb\xcc\xad'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
