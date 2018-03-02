from clove.network.bitcoin import Bitcoin


class Cinder(Bitcoin):
    """
    Class with all the necessary Cinder network information based on
    https://github.com/CrypTraider/Cinder/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'cinder'
    symbols = ('CIN', )
    nodes = ("104.156.253.23",
             "108.61.223.155",
             "104.236.49.247",
             "128.199.57.33")
    port = 22555
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 163
    }

# Has no testnet
