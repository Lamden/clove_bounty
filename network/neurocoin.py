from clove.network.bitcoin import Bitcoin


class Neurocoin(Bitcoin):
    """
    Class with all the necessary Neurocoin network information based on
    https://github.com/neurocoin/neurocoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'neurocoin'
    symbols = ('NRO', )
    nodes = ("46.101.192.195",
             "188.226.150.84",
             "147.135.191.162")
    port = 17771
    message_start = b'\xe6\xe8\xe9\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 53,
        'SCRIPT_ADDR': 117,
        'SECRET_KEY': 181
    }
