from clove.network.bitcoin import Bitcoin


class BetaCoin(Bitcoin):
    """
    Class with all the necessary BetaCoin network information based on
    https://github.com/BetaCoinDev/betacoin/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'betacoin'
    symbols = ('BET', )
    seeds = ("seed1.betacoin.org",
             "seed2.betacoin.org",
             "seed3.betacoin.org",
             "seed4.betacoin.org",
             "seed5.betacoin.org",
             "seed6.betacoin.org")
    port = 32333
    message_start = b'\xa5\xc0\x79\x55'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 11,
        'SECRET_KEY': 143
    }


class BetaCoinTestNet(BetaCoin):
    """
    Class with all the necessary BetaCoin testing network information based on
    https://github.com/BetaCoinDev/betacoin/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-betacoin'
    seeds = ("xjo-test1.twilightparadox.com", )
    port = 26783
    message_start = b'\x0a\xc0\x73\x12'
    base58_prefixes = {
        'PUBKEY_ADDR': 83,
        'SCRIPT_ADDR': 13,
        'SECRET_KEY': 212
    }
