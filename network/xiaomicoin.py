from clove.network.bitcoin import Bitcoin


class Xiaomicoin(Bitcoin):
    """
    Class with all the necessary Xiaomicoin network information based on
    https://github.com/xiaomicoin/Xiaomicoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'xiaomicoin'
    symbols = ('MI', )
    nodes = ("120.25.158.22",
             "121.42.12.176")
    port = 27896
    message_start = b'\xce\xfb\xfa\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 75,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 203
    }

# no testnet
