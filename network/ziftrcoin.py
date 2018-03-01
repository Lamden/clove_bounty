from clove.network.bitcoin import Bitcoin


class ZiftrCOIN(Bitcoin):
    """
    Class with all the necessary ZiftrCOIN network information based on
    https://github.com/ZiftrCOIN/ziftrcoin/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'ziftrcoin'
    symbols = ('ZRC', )
    seeds = ("seed.ziftrcoin.com")
    port = 10333
    message_start = b'\x9e\xee\x83\x2b'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }


class ZiftrCOINTestNet(ZiftrCOIN):
    """
    Class with all the necessary ZiftrCOIN testing network information based on
    https://github.com/ZiftrCOIN/ziftrcoin/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-ziftrcoin'
    seeds = ("testnet-seed1.ziftrcoin.com")
    port = 11333
