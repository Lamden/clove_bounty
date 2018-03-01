from clove.network.bitcoin import Bitcoin


class FujiCoin(Bitcoin):
    """
    Class with all the necessary FJC network information based on
    https://github.com/fujicoin/fujicoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'fujicoin'
    symbols = ('FJC', )
    seeds = ()
    port = 3777
    message_start = b'\x66\x75\x6a\x69'
    base58_prefixes = {
        'PUBKEY_ADDR': 36,
        'SCRIPT_ADDR': 16,
        'SECRET_KEY': 164
    }


class FujiCoinTestNet(FujiCoin):
    """
    Class with all the necessary FJC testing network information based on
    https://github.com/fujicoin/fujicoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-fujicoin'
    seeds = ()
    port = 13777
    message_start = b'\x69\x6a\x75\x66'
    base58_prefixes = {
        'PUBKEY_ADDR': 74,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 202
    }
