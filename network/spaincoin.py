from clove.network.bitcoin import Bitcoin


class Spaincoin(Bitcoin):
    """
    Class with all the necessary Spaincoin network information based on
    https://github.com/SpainCoinProject/spaincoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'spaincoin'
    symbols = ('DMD', )
    seeds = ("dnsseed.ds.spaincoin.org",
             "dnsseed.spaincoin.org")
    port = 11492
    message_start = b'\xfb\x14\x92\x00'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 191
    }


class SpaincoinTestNet(Spaincoin):
    """
    Class with all the necessary Spaincoin testing network information based on
    https://github.com/SpainCoinProject/spaincoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-spaincoin'
    seeds = ("dnsseed.spaincoin.org", )
    port = 21492
    message_start = b'\xfd\xc2\xb8\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
