from clove.network.bitcoin import Bitcoin


class Vipercoin(Bitcoin):
    """
    Class with all the necessary Vipercoin network information based on
    https://github.com/joejoemister/vipercoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'vipercoin'
    symbols = ('VIPER', )
    seeds = ("165.227.96.129",
             "71.150.156.246")
    port = 9333
    message_start = b'\xf9\xbe\xb4\xd2'
    base58_prefixes = {
        'PUBKEY_ADDR': 26,
        'SCRIPT_ADDR': 7,
        'SECRET_KEY': 154
    }
