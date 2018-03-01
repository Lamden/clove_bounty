
from clove.network.bitcoin import Bitcoin


class WayGuide(Bitcoin):
    """
    Class with all the necessary WAY network information based on
    https://github.com/wayguide/waycoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'wayguide'
    symbols = ('WAY', )
    seeds = ()
    port = 21000
    message_start = b'\x57\x41\x59\x47'
    base58_prefixes = {
        'PUBKEY_ADDR': 73,
        'SCRIPT_ADDR': 97,
        'SECRET_KEY': 173
    }


class WayGuideTestNet(WayGuide):
    """
    Class with all the necessary WAY testing network information based on
    https://github.com/wayguide/waycoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-wayguide'
    seeds = ()
    port = 22000
    message_start = b'\x77\x61\x79\x67'
    base58_prefixes = {
        'PUBKEY_ADDR': 135,
        'SCRIPT_ADDR': 208,
        'SECRET_KEY': 249
    }
