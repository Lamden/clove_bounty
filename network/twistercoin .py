from clove.network.bitcoin import Bitcoin


class Twistercoin(Bitcoin):
    """
    Class with all the necessary Twistercoin network information based on
    https://github.com/miningfool/twistercoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'twistercoin'
    symbols = ('TWIST', )
    nodes = ("52.10.32.200", )
    port = 44258
    message_start = b'\xf3\x2d\xa5\x71'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 73,
        'SECRET_KEY': 193
    }

# no testnet
