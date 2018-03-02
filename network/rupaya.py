from clove.network.bitcoin import Bitcoin


class Rupaya(Bitcoin):
    """
    Class with all the necessary Rupaya network information based on
    https://github.com/rupaya-project/rupaya/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'rupaya'
    symbols = ('RUPX', )
    seeds = ("dns.rupx.io", )
    port = 9020
    message_start = b'\x63\x43\x49\x56'
    base58_prefixes = {
        'PUBKEY_ADDR': 15,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 212
    }


class RupayaTestNet(Rupaya):
    """
    Class with all the necessary Rupaya testing network information based on
    https://github.com/rupaya-project/rupaya/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-rupaya'
    seeds = ()
    nodes = ("207.148.0.129",
             "45.77.239.30",
             "45.76.226.204")
    port = 51434
    message_start = b'\x43\x76\x65\xba'
    base58_prefixes = {
        'PUBKEY_ADDR': 139,
        'SCRIPT_ADDR': 19,
        'SECRET_KEY': 239
    }
