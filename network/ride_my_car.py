
from clove.network.bitcoin import Bitcoin


class RideMyCar(Bitcoin):
    """
    Class with all the necessary RIDE network information based on
    http://www.github.com/RideMyCar/RideMyCar-Coin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'ride-my-car'
    symbols = ('RIDE', )
    nodes = ('146.185.146.172', )
    port = 11517
    message_start = b'\x22\x50\x70\x35'
    base58_prefixes = {
        'PUBKEY_ADDR': 61,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 166
    }


class RideMyCarTestNet(RideMyCar):
    """
    Class with all the necessary RIDE testing network information based on
    http://www.github.com/RideMyCar/RideMyCar-Coin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-ride-my-car'
    seeds = ()
    port = 25713
    message_start = b'\xfe\x0c\x2f\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 112,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 240
    }
