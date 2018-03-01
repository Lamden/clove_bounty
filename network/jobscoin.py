from clove.network.bitcoin import Bitcoin


class JobsCoin(Bitcoin):
    """
    Class with all the necessary JobsCoin network information based on
    https://github.com/jobscoindev/jobscoin-source/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'jobscoin'
    symbols = ('JOBS', )
    seeds = ("seed1.jobscoin.us",
             "seed2.jobscoin.us",
             "seed3.jobscoin.us",
             "seed4.jobscoin.us")
    port = 9999
    message_start = b'\x1a\x2c\x1b\x3c'
    base58_prefixes = {
        'PUBKEY_ADDR': 43,
        'SCRIPT_ADDR': 44,
        'SECRET_KEY': 171
    }

# No testnet
