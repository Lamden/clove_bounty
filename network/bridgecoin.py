from clove.network.bitcoin import Bitcoin


class BridgeCoin(Bitcoin):
    """
    Class with all the necessary BridgeCoin network information based on
    https://github.com/CryptoBridge/bridgecoin/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'bridgecoin'
    symbols = ('BCO', )
    seeds = ("seed1.bridgecoin.org",
             "seed2.bridgecoin.org",
             "seed3.bridgecoin.org")
    port = 6333
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 27,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 176
    }


class BridgeCoinTestNet(BridgeCoin):
    """
    Class with all the necessary BridgeCoin testing network information based on
    https://github.com/CryptoBridge/bridgecoin/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-bridgecoin'
    seeds = ("seed1.bridgecoin.org",
             "seed2.bridgecoin.org",
             "seed3.bridgecoin.org")
    port = 16333
    message_start = b'\xfd\xd2\xc8\xf1'
    base58_prefixes = {
        'PUBKEY_ADDR': 10,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
