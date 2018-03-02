from clove.network.bitcoin import Bitcoin


class EbolaShare(Bitcoin):
    """
    Class with all the necessary EbolaShare network information based on
    https://github.com/Ebolashare/ebolashare/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'ebolashare'
    symbols = ('EBS', )
    nodes = ("37.25.41.54", )
    port = 9333
    message_start = b'\xe2\xe1\xe2\xe1'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 93,
        'SECRET_KEY': 161
    }

# no testnet
