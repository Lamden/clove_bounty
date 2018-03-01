from clove.network.bitcoin import Bitcoin


class GeoCoin(Bitcoin):
    """
    Class with all the necessary GeoCoin network information based on
    https://github.com/onetimer/onetimer/blob/master/src/net.cpp
    (date of access: 02/22/2018)
    """
    name = 'geocoin'
    symbols = ('GEO', )
    seeds = ("104.236.52.122")
    port = 9748
    message_start = b'\xae\xbf\xc0\xd1'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 166
    }


class GeoCoinTestNet(GeoCoin):
    """
    Class with all the necessary GeoCoin testing network information based on
    https://github.com/onetimer/onetimer/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'test-geocoin'
    seeds = ("104.236.52.122")
    port = 9748
