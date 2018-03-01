from clove.network.bitcoin import Bitcoin


class Wisdomcoin(Bitcoin):
    """
    Class with all the necessary Wisdomcoin network information based on
    https://github.com/wisdomcoin/SourceCode/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'wisdomcoin'
    symbols = ('WISC', )
    seeds = ("35.163.177.45",
             "95.211.57.108")
    port = 17771
    message_start = b'\xeb\x3d\x1c\xc4'
    base58_prefixes = {
        'PUBKEY_ADDR': 73,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 201
    }
