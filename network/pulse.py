from clove.network.bitcoin import Bitcoin


class Pulse(Bitcoin):
    """
    Class with all the necessary Pulse network information based on
    https://github.com/elcrypto/pulse/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'pulse'
    symbols = ('PULSE', )
    nodes = ("52.34.51.188", )
    port = 57152
    message_start = b'\xfc\xf9\xb9\xf3'
    base58_prefixes = {
        'PUBKEY_ADDR': 51,
        'SCRIPT_ADDR': 26,
        'SECRET_KEY': 179
    }


# No Testnet
