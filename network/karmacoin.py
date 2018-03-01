from clove.network.bitcoin import Bitcoin


class Karmacoin(Bitcoin):
    """
    Class with all the necessary Karmacoin (KARMA) network information based on
    https://github.com/karmateam/karma/blob/master-0.8/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'karmacoin'
    symbols = ('KARMA', )
    seeds = ('karmaseeder.alltheco.in', )
    port = 9432
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 45,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 173
    }


class KarmacoinTestNet(Karmacoin):
    """
    Class with all the necessary Karmacoin (KARMA) testing network information based on
    https://github.com/karmateam/karma/blob/master-0.8/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-karmacoin'
    seeds = ('testnet-karmaseeder.alltheco.in', )
    port = 19432
