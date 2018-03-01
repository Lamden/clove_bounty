from clove.network.bitcoin import Bitcoin


class Pesobit(Bitcoin):
    """
    Class with all the necessary Pesobit network information based on
    https://github.com/pesobitph/pesobit-source/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'pesobit'
    symbols = ('PSB', )
    seeds = ("212.24.104.88")
    port = 7867
    message_start = b'\xea\xaf\xe3\xc7'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 183
    }

# no testnet
