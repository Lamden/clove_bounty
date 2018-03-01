from clove.network.bitcoin import Bitcoin


class Joincoin(Bitcoin):
    """
    Class with all the necessary joincoin network information based on
    https://github.com/joincoin/joincoin/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'joincoin'
    symbols = ('J', )
    seeds = ("seed1.joincoin.org",
             "seed2.joincoin.org",
             "seed3.joincoin.org",
             "seed4.joincoin.org")
    port = 17941
    message_start = b'\xf1\xb4\xdc\x9e'
    base58_prefixes = {
        'PUBKEY_ADDR': 43,
        'SCRIPT_ADDR': 9,
        'SECRET_KEY': 178
    }


class JoincoinTestNet(Joincoin):
    """
    Class with all the necessary Joincoin testing network information based on
    https://github.com/joincoin/joincoin/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-joincoin'
    seeds = ("testseed1.joincoin.org", )
    port = 27941
    message_start = b'\x5a\x7b\xff\xfa'
    base58_prefixes = {
        'PUBKEY_ADDR': 88,
        'SCRIPT_ADDR': 188,
        'SECRET_KEY': 239
    }
