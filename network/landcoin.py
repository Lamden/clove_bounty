from clove.network.bitcoin import Bitcoin


class LandCoin(Bitcoin):
    """
    Class with all the necessary LandCoin network information based on
    https://github.com/landcoin-project/landcoin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'landcoin'
    symbols = ('LND', )
    seeds = ("seed.landcoin.net")
    port = 1911
    message_start = b'\xf9\xbe\xb4\xd2'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 176
    }


class LandCoinTestNet(LandCoin):
    """
    Class with all the necessary LandCoin testing network information based on
    https://github.com/landcoin-project/landcoin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-landcoin'
    seeds = ("seed.landcoin.net")
    port = 11911
    message_start = b'\x0b\x11\x09\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
