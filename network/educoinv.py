from clove.network.bitcoin import Bitcoin


class EducoinV(Bitcoin):
    """
    Class with all the necessary EducoinV network information based on
    https://github.com/crypto-dev/educoin_v2/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'educoinv'
    symbols = ('EDC', )
    nodes = ("5.9.165.252", "159.203.123.176", )
    port = 6677
    message_start = b'\xbe\x18\xe9\x1d'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 161
    }
