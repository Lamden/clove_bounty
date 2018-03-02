from clove.network.bitcoin import Bitcoin


class Autumncoin(Bitcoin):
    """
    Class with all the necessary Autumncoin network information based on
    https://github.com/Autumncoindev/ATM/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'autumncoin'
    symbols = ('ATM', )
    nodes = ("192.241.204.48", )
    port = 58851
    message_start = b'\x55\x52\x12\x0d'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 151
    }

# Has no testnet
