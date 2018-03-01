from clove.network.bitcoin import Bitcoin


class DynamicCoin(Bitcoin):
    """
    Class with all the necessary DynamicCoin (DMC) network information based on
    https://github.com/DynamicCoinOrg/DMC/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'dynamiccoin'
    symbols = ('DMC', )
    seeds = ('main.seeds.dynamiccoin.net')
    port = 7333
    message_start = b'\xf9\xbe\xb4\xe0'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


class DynamicCoinTestNet(DynamicCoin):
    """
    Class with all the necessary DynamicCoin (DMC) testing network information based on
    https://github.com/DynamicCoinOrg/DMC/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-dynamiccoin'
    seeds = ('test.seeds.dynamiccoin.net')
    port = 17333
    message_start = b'\x0b\x11\x09\x08'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
