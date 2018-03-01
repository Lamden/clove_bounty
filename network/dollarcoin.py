from clove.network.bitcoin import Bitcoin


class DollarCoin(Bitcoin):
    """
    Class with all the necessary DLC network information based on
    https://github.com/dollarcoins/source/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'dollarcoin'
    symbols = ('DLC', )
    seeds = ()
    port = 8145
    message_start = b'\xfc\x9b\x3d\x41'
    base58_prefixes = {
        'PUBKEY_ADDR': 30,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 158
    }


class DollarCoinTestNet(DollarCoin):
    """
    Class with all the necessary DLC testing network information based on
    https://github.com/dollarcoins/source/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-dollarcoin'
    seeds = ()
    port = 18145
    message_start = b'\xd5\xac\xae\x18'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
