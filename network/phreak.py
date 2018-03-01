from clove.network.bitcoin import Bitcoin


class Phreak(Bitcoin):
    """
    Class with all the necessary Phreak network information based on
    https://github.com/qtvideofilter/streamingcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'phreak'
    symbols = ('PHR', )
    nodes = ("52.26.166.22", )
    port = 4744
    message_start = b'\x2d\x3f\xa2\xf5'
    base58_prefixes = {
        'PUBKEY_ADDR': 24,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 152
    }

# no testnet
