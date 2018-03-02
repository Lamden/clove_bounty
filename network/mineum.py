from clove.network.bitcoin import Bitcoin


class Mineum(Bitcoin):
    """
    Class with all the necessary Mineum network information based on
    https://github.com/antho281/mineum/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Mineum'
    symbols = ('MNM', )
    seeds = ('nodes.muex.io', )
    port = 31316
    message_start = b'\x5a\xc3\x82\xd3'
    base58_prefixes = {
        'PUBKEY_ADDR': 51,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 179
    }


# Has no Testnet
