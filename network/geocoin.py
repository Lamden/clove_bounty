from clove.network.bitcoin import Bitcoin


class GeoCoin(Bitcoin):
    """
    Class with all the necessary GeoCoin network information based on
    https://github.com/onetimer/onetimer/blob/master/src/net.cpp
    (date of access: 02/22/2018)
    """
    name = 'geocoin'
    symbols = ('GEO', )
    nodes = ("104.236.52.122", )
    port = 9748
    message_start = b'\xae\xbf\xc0\xd1'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 166
    }
