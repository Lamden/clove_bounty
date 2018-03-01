from clove.network.bitcoin import Bitcoin


class Bithire(Bitcoin):
    """
    Class with all the necessary Bithire network information based on
    https://github.com/Bithire/Bithire/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bithire'
    symbols = ('HIRE', )
    seeds = ("46.101.3.80")
    port = 11816
    message_start = b'\x07\xa1\x11\xb3'
    base58_prefixes = {
        'PUBKEY_ADDR': 40,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 168
    }

# Has no testnet
