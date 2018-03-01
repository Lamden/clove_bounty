
from clove.network.bitcoin import Bitcoin


class Ugain(Bitcoin):
    """
    Class with all the necessary GAIN network information based on
    https://github.com/ugain1/ugain-src/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'ugain'
    symbols = ('GAIN', )
    seeds = ()
    port = 7891
    message_start = b'\x06\xbb\xe2\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 166
    }


class UgainTestNet(Ugain):
    """
    Class with all the necessary GAIN testing network information based on
    https://github.com/ugain1/ugain-src/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-ugain'
    seeds = ()
    port = 17891
    message_start = b'\x8b\xcf\xc3\x9a'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
