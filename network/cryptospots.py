from clove.network.bitcoin import Bitcoin


class CryptoSpots(Bitcoin):
    """
    Class with all the necessary CryptoSpots network information based on
    https://github.com/xPooky/CryptoSpots/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'cryptospots'
    symbols = ('CS', )
    nodes = ("45.55.243.122",
             "104.236.84.239",
             "104.236.83.193")
    port = 17771
    message_start = b'\x1d\xc2\x3d\x1a'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 156
    }

# Has no testnet
