from clove.network.bitcoin import Bitcoin


class Concoin(Bitcoin):
    """
    Class with all the necessary Concoin network information based on
    https://github.com/Concoin/concoin-master/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'concoin'
    symbols = ('CONX', )
    nodes = ("94.176.236.84",
             "212.47.238.107",
             "94.176.235.111")
    port = 40100
    message_start = b'\xc1\xc2\xc5\xb4'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 23,
        'SECRET_KEY': 156
    }
