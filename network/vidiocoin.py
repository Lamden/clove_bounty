from clove.network.bitcoin import Bitcoin


class Vidiocoin(Bitcoin):
    """
    Class with all the necessary Vidiocoin network information based on
    https://github.com/vidioshare/vidio/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'vidiocoin'
    symbols = ('VDO', )
    nodes = ("212.91.189.164",
             "195.34.100.2")
    port = 23682
    message_start = b'\xfa\xf2\xef\xb4'
    base58_prefixes = {
        'PUBKEY_ADDR': 70,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 198
    }

# no testnet
