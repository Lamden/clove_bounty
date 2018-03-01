from clove.network.bitcoin import Bitcoin


class Indicoin(Bitcoin):
    """
    Class with all the necessary Indicoin network information based on
    https://github.com/sarkarrajsingh1/indicoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'indicoin'
    symbols = ('INDI', )
    seeds = ("dnsseed.inditrades.org")
    port = 7366
    message_start = b'\xe4\xe8\xe9\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 153
    }

# no testnet
