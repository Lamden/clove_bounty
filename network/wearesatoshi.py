from clove.network.bitcoin import Bitcoin


class WeAreSatoshi(Bitcoin):
    """
    Class with all the necessary WeAreSatoshi network information based on
    https://github.com/WeAreSatoshi/WeAreSatoshi2/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'wearesatoshi'
    symbols = ('WSX', )
    seeds = ("wsx.dnsseed.crypto2.net", )
    port = 8922
    message_start = b'\xFA\x4D\x44\xFC'
    base58_prefixes = {
        'PUBKEY_ADDR': 135,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 263
    }

# no testnet
