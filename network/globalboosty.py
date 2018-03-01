from clove.network.bitcoin import Bitcoin


class GlobalBoostY(Bitcoin):
    """
    Class with all the necessary BSTY network information based on
    http://www.github.com/GlobalBoost/GlobalBoost-Y/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'globalboosty'
    symbols = ('BSTY', )
    seeds = ('seeder.globalboost.info', 'seeder2.globalboost.info', )
    port = 8226
    message_start = b'\xa2\xb2\xe2\xf2'
    base58_prefixes = {
        'PUBKEY_ADDR': 77,
        'SCRIPT_ADDR': 139,
        'SECRET_KEY': 205
    }


class GlobalBoostYTestNet(GlobalBoostY):
    """
    Class with all the necessary BSTY testing network information based on
    http://www.github.com/GlobalBoost/GlobalBoost-Y/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-globalboost-y'
    seeds = ('testnet-seeder.globalboost.info', )
    port = 18226
    message_start = b'bsty'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
