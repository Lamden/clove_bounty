from clove.network.bitcoin import Bitcoin


class HighGain(Bitcoin):
    """
    Class with all the necessary  High Gain (HIGH) network information based on
    https://github.com/highgainqubit/highgain/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'highgain'
    symbols = ('HIGH', )
    seeds = ('34.214.230.207')
    port = 4664
    message_start = b'\x2d\x3f\xa2\xf5'
    base58_prefixes = {
        'PUBKEY_ADDR': 42,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 170
    }


# no testnet
