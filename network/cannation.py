from clove.network.bitcoin import Bitcoin


class Cannation(Bitcoin):
    """
    Class with all the necessary Cannation network information based on
    https://github.com/cannationproject/cannation/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Cannation'
    symbols = ('CNNC', )
    seeds = ("195.74.52.227", "149.56.154.65")
    port = 12367
    message_start = b'\x52\x56\x8b\x9e'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 156
    }


# Has no Testnet
